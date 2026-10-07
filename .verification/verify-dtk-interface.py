#!/usr/bin/env python3
"""Verify DTK interface inventory against local source checkouts.

This checks declarations, exports, documentation structure and links.
Capabilities and runtime behavior still require the review described in the plan.
"""

import argparse
import json
import re
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
DECLARATION = re.compile(
    r"(?<!enum )\b(?:class|struct)\s+"
    r"(?:[A-Z_][A-Z_0-9]*(?:\([^)]*\))?\s+)*(\w+)"
    r"(?:\s*<[^;{}]*?>)?(?:\s+final)?\s*(?::[^;{]+)?\s*\{"
)


def source_text(path):
    text = re.sub(r"/\*.*?\*/|//[^\n]*", "", path.read_text(), flags=re.S)
    return re.sub(r"^\s*#.*$", "", text, flags=re.M)


def named_elements(paths):
    return {
        name
        for path in paths
        for name in re.findall(r"QML_NAMED_ELEMENT\(\s*(\w+)\s*\)", source_text(path))
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path.home() / "repo")
    args = parser.parse_args()
    root = args.source_root.resolve()
    manifest = json.loads((REPO / ".verification/dtk-interface-manifest.json").read_text())
    missing_projects = [project for project in manifest["source_revisions"] if not (root / project).is_dir()]
    if missing_projects:
        for project in missing_projects:
            print(f"NOT FOUND: source checkout {root / project}")
        return 1
    documents = manifest["documents"]
    failures = []
    not_found = []
    count = 0

    for relative, entries in documents.items():
        path = REPO / relative
        text = path.read_text()
        sections = re.findall(r"^### ([^\n]+)\n(.*?)(?=^### |\Z)", text, re.M | re.S)
        sections = [(name, body) for name, body in sections if name not in {"CMake 配置", "使用方式"}]
        actual = [name for name, _ in sections]
        if len(actual) != len(set(actual)) or set(actual) != set(entries):
            failures.append(f"{relative}: section inventory differs from manifest")
        for name, body in sections:
            if re.findall(r"^#### (.+)$", body, re.M) != ["定位", "功能能力总结", "使用场景"]:
                failures.append(f"{relative}: {name} has incorrect subsections")
        for name, entry in entries.items():
            count += 1
            source = root / entry["source"]
            if not source.is_file():
                not_found.append(f"{name}: {source}")
                continue
            raw = source_text(source)
            kind = entry["kind"]
            symbol = entry["symbol"]
            if kind == "cpp-type":
                found = symbol in DECLARATION.findall(raw)
                # Nested definitions must also name their enclosing type/namespace.
                if "::" in name:
                    found = found and name.split("::")[0] in raw
            elif kind == "qml-named":
                found = bool(re.search(r"QML_NAMED_ELEMENT\(\s*" + re.escape(name) + r"\s*\)", raw))
            elif kind == "qml-registration":
                found = bool(re.search(r'"' + re.escape(name) + r'"', raw))
            elif kind == "qml-file":
                found = source.stem == name
            elif kind == "function":
                found = bool(re.search(r"\b" + re.escape(symbol) + r"\s*\(", raw))
            else:
                found = False
            if not found:
                not_found.append(f"{name}: declaration missing in {entry['source']}")
        print(f"{relative}: {len(entries)} entries checked")

    # Scan definitions in public headers, including legacy conditional branches.
    # Explicit exclusions are implementation helpers, not consumer interfaces.
    excluded = manifest["excluded_implementation_types"]
    for project in ("dtkcore", "dtkgui", "dtkwidget"):
        documented = {
            (entry["source"], entry["symbol"])
            for entries in documents.values()
            for entry in entries.values()
            if entry["kind"] == "cpp-type"
        }
        for path in sorted((root / project / "include").rglob("*.h")):
            if "private" in path.parts or path.name.endswith("_p.h"):
                continue
            relative = path.relative_to(root).as_posix()
            for symbol in DECLARATION.findall(source_text(path)):
                if (relative, symbol) not in documented and symbol not in excluded.get(relative, []):
                    failures.append(f"undocumented public-header definition: {relative}: {symbol}")

    declarative = root / "dtkdeclarative"
    cpp_public = (declarative / "src/src.cmake").read_text()
    for header in set(re.findall(r"\$\{PROJECT_SOURCE_DIR\}/src/(\w+\.h)", cpp_public)):
        if header == "dtkdeclarative_global.h":
            continue
        relative = "dtkdeclarative/src/" + header
        for symbol in DECLARATION.findall(source_text(root / relative)):
            if not any(entry["source"] == relative and entry["symbol"] == symbol
                       for entries in documents.values() for entry in entries.values()):
                failures.append(f"undocumented declarative public type: {relative}: {symbol}")

    qml_list = source_text(declarative / "qt6/src/qml.cmake")
    expected_main = set(re.findall(r'"qml/(\w+)\.qml"', qml_list))
    settings_header = declarative / "src/private/dsettingscontainer_p.h"
    expected_main |= named_elements(
        [p for p in (declarative / "src").rglob("*.h") if p != settings_header]
        + [declarative / "qt6/src/dquickextendregister_p.h"]
    )
    # These are registered explicitly by registerTypes(), rather than qt_add_qml_module().
    plugin = source_text(declarative / "qmlplugin/qmlplugin_plugin.cpp")
    dynamic_main = {"InWindowBlur", "SortFilterProxyModel", "Style", "ColorOverlay", "OpacityMask"}
    for name in dynamic_main:
        if not re.search(r'"' + name + r'"', plugin):
            not_found.append(f"explicit QML registration: {name}")
    expected_main |= dynamic_main
    main_document = "skills/dtk/interface/dtkdeclarative/org.deepin.dtk.md"
    if expected_main != set(documents[main_document]):
        failures.append(f"QML main export mismatch: {sorted(expected_main ^ set(documents[main_document]))}")

    settings_cmake = source_text(declarative / "qt6/src/qml/settings/CMakeLists.txt")
    expected_settings = set(re.findall(r"\b(\w+)\.qml\b", settings_cmake)) | named_elements([settings_header])
    settings_document = "skills/dtk/interface/dtkdeclarative/org.deepin.dtk.settings.md"
    if expected_settings != set(documents[settings_document]):
        failures.append(f"QML settings export mismatch: {sorted(expected_settings ^ set(documents[settings_document]))}")

    for path in [REPO / p for p in documents] + [REPO / "skills/dtk/SKILL.md"]:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#")[0]
            if not (path.parent / target).exists():
                failures.append(f"broken link in {path.relative_to(REPO)}: {target}")

    for project, revision in manifest["source_revisions"].items():
        current = subprocess.check_output(["git", "-C", str(root / project), "rev-parse", "HEAD"], text=True).strip()
        if current != revision:
            failures.append(f"{project}: source revision changed; review capabilities and update inventory")
    for error in failures:
        print("FAIL:", error)
    for error in not_found:
        print("NOT FOUND:", error)
    print(f"Inventory: {count} entries; FAIL: {len(failures)}; NOT FOUND: {len(not_found)}")
    if not failures and not not_found:
        print("PASS: declarations, export coverage, section structure and file links")
    return int(bool(failures or not_found))


if __name__ == "__main__":
    raise SystemExit(main())
