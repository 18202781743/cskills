# DTK 接口完整使用统计（按频次排序）

## 项目信息

- **分析项目**: 43 个 DDE/Deepin 项目（/home/uos/ai-skills/repo/）
- **排除项目**: dtk 相关项目
- **分析时间**: 2026-07-13
- **统计范围**: C++ 源文件 9242 个 + QML/JS 文件 824 个

---

## 一、C++ 头文件引用频率（#include <D*>，全部）

| 排名 | 头文件 | 引用次数 | 所属模块 |
|------|--------|---------|---------|
| 1 | DGuiApplicationHelper | 398 | dtkgui |
| 2 | DFontSizeManager | 233 | dtkgui |
| 3 | DLabel | 227 | dtkwidget |
| 4 | DApplication | 214 | dtkwidget |
| 5 | DConfig | 178 | dtkcore |
| 6 | DDialog | 126 | dtkwidget |
| 7 | DWidget | 116 | dtkwidget |
| 8 | DSysInfo | 93 | dtkcore |
| 9 | DStyle | 89 | dtkwidget |
| 10 | DIconButton | 89 | dtkwidget |
| 11 | DApplicationHelper | 85 | dtkgui |
| 12 | DPalette | 80 | dtkgui |
| 13 | DDBusSender | 80 | dtkcore |
| 14 | DPushButton | 79 | dtkwidget |
| 15 | DLog | 72 | dtkcore |
| 16 | DListView | 69 | dtkwidget |
| 17 | DFrame | 69 | dtkwidget |
| 18 | DSpinner | 66 | dtkwidget |
| 19 | DPaletteHelper | 59 | dtkgui |
| 20 | DBlurEffectWidget | 58 | dtkwidget |
| 21 | DWindowManagerHelper | 49 | dtkgui |
| 22 | DLineEdit | 47 | dtkwidget |
| 23 | DMenu | 43 | dtkwidget |
| 24 | DTitlebar | 41 | dtkwidget |
| 25 | DTipLabel | 40 | dtkwidget |
| 26 | DCommandLinkButton | 40 | dtkwidget |
| 27 | DSuggestButton | 39 | dtkwidget |
| 28 | DHiDPIHelper | 29 | dtkgui |
| 29 | DStyleHelper | 28 | dtkwidget |
| 30 | DDBusInterface | 28 | dtkcore |
| 31 | DToolButton | 27 | dtkwidget |
| 32 | DDesktopServices | 27 | dtkcore |
| 33 | DSwitchButton | 25 | dtkwidget |
| 34 | DPasswordEdit | 25 | dtkwidget |
| 35 | DButtonBox | 25 | dtkwidget |
| 36 | DWidgetUtil | 24 | dtkwidget |
| 37 | DPlatformWindowHandle | 24 | dtkgui |
| 38 | DComboBox | 24 | dtkwidget |
| 39 | DSettingsOption | 23 | dtkwidget |
| 40 | DMainWindow | 23 | dtkwidget |
| 41 | DToolTip | 22 | dtkwidget |
| 42 | DFloatingButton | 22 | dtkwidget |
| 43 | DArrowRectangle | 22 | dtkwidget |
| 44 | DPlatformTheme | 21 | dtkgui |
| 45 | DBackgroundGroup | 21 | dtkwidget |
| 46 | DStackedWidget | 20 | dtkwidget |
| 47 | DSlider | 20 | dtkwidget |
| 48 | DCheckBox | 20 | dtkwidget |
| 49 | DSingleton | 18 | dtkcore |
| 50 | DDciIcon | 17 | dtkgui |
| 51 | DWaterProgress | 15 | dtkwidget |
| 52 | DUtil | 15 | dtkcore |
| 53 | DStyleOption | 15 | dtkwidget |
| 54 | DStyledItemDelegate | 15 | dtkwidget |
| 55 | DIconTheme | 15 | dtkgui |
| 56 | DFileDialog | 15 | dtkwidget |
| 57 | DStandardItem | 14 | dtkwidget |
| 58 | DPinyin | 14 | dtkcore |
| 59 | DObject | 14 | dtkcore |
| 60 | DMessageManager | 14 | dtkwidget |
| 61 | DTableView | 13 | dtkwidget |
| 62 | DRegionMonitor | 13 | dtkcore |
| 63 | DNotifySender | 13 | dtkcore |
| 64 | DDesktopEntry | 13 | dtkcore |
| 65 | DTreeView | 12 | dtkwidget |
| 66 | DHeaderView | 12 | dtkwidget |
| 67 | DAnchors | 12 | dtkcore |
| 68 | DTextEdit | 11 | dtkwidget |
| 69 | DSettings | 11 | dtkwidget |
| 70 | DProgressBar | 11 | dtkwidget |
| 71 | DFloatingMessage | 11 | dtkwidget |
| 72 | DSpinBox | 10 | dtkwidget |
| 73 | DSettingsDialog | 10 | dtkwidget |
| 74 | DIcon | 10 | dtkgui |
| 75 | DHorizontalLine | 10 | dtkwidget |
| 76 | DStandardPaths | 9 | dtkcore |
| 77 | DScrollArea | 9 | dtkwidget |
| 78 | DFloatingWidget | 9 | dtkwidget |
| 79 | DArrowLineDrawer | 9 | dtkwidget |
| 80 | DSGApplication | 8 | dtkcore |
| 81 | DSearchEdit | 8 | dtkwidget |
| 82 | DDBusExtendedAbstractInterface | 8 | dtkcore |
| 83 | DAbstractDialog | 8 | dtkwidget |
| 84 | DWarningButton | 7 | dtkwidget |
| 85 | DVerticalLine | 7 | dtkwidget |
| 86 | DSettingsWidgetFactory | 7 | dtkwidget |
| 87 | DRadioButton | 7 | dtkwidget |
| 88 | DFileChooserEdit | 7 | dtkwidget |
| 89 | DStyleOptionButton | 6 | dtkwidget |
| 90 | DSizeMode | 6 | dtkgui |
| 91 | DAccessibilityChecker | 6 | dtkcore |
| 92 | DTextBrowser | 5 | dtkwidget |
| 93 | DMessageBox | 5 | dtkwidget |
| 94 | DDialogCloseButton | 5 | dtkwidget |
| 95 | DCrumbEdit | 5 | dtkwidget |
| 96 | DTextEncoding | 4 | dtkcore |
| 97 | DTableWidget | 4 | dtkwidget |
| 98 | DSimpleListView | 4 | dtkwidget |
| 99 | DRecentManager | 4 | dtkcore |
| 100 | DPlatformHandle | 4 | dtkgui |
| 101 | DListWidget | 4 | dtkwidget |
| 102 | DExpected | 4 | dtkcore |
| 103 | DClipEffectWidget | 4 | dtkwidget |
| 104 | DApplicationSettings | 4 | dtkwidget |
| 105 | DTrashManager | 3 | dtkcore |
| 106 | DPlainTextEdit | 3 | dtkwidget |
| 107 | DImageButton | 3 | dtkwidget |
| 108 | DForeignWindow | 3 | dtkgui |
| 109 | DFontManager | 3 | dtkgui |
| 110 | DErrorMessage | 3 | dtkwidget |
| 111 | DWindowMinButton | 2 | dtkwidget |
| 112 | DWindowMaxButton | 2 | dtkwidget |
| 113 | DWindowCloseButton | 2 | dtkwidget |
| 114 | DTreeWidget | 2 | dtkwidget |
| 115 | DThumbnailProvider | 2 | dtkgui |
| 116 | DStylePainter | 2 | dtkwidget |
| 117 | DSplitter | 2 | dtkwidget |
| 118 | DShadowLine | 2 | dtkgui |
| 119 | DPathBuf | 2 | dtkcore |
| 120 | DDrawer | 2 | dtkwidget |
| 121 | DWindowOptionButton | 1 | dtkwidget |
| 122 | DTabBar | 1 | dtkwidget |
| 123 | DSvgRenderer | 1 | dtkgui |
| 124 | DSimpleListItem | 1 | dtkwidget |
| 125 | DSecureString | 1 | dtkcore |
| 126 | DOcr | 1 | dtkwidget |
| 127 | DKeySequenceEdit | 1 | dtkwidget |
| 128 | DInputDialog | 1 | dtkwidget |
| 129 | DGroupBox | 1 | dtkwidget |
| 130 | DGraphicsView | 1 | dtkwidget |
| 131 | DFileWatcherManager | 1 | dtkcore |
| 132 | DFileSystemWatcher | 1 | dtkcore |
| 133 | DFileIconProvider | 1 | dtkwidget |
| 134 | DColoredProgressBar | 1 | dtkwidget |
| 135 | DCalendarWidget | 1 | dtkwidget |
| 136 | DBusExtendedAbstractInterface | 1 | dtkcore |
| 137 | DBlurEffectWithBorderWidget | 1 | dtkwidget |
| 138 | DAlertControl | 1 | dtkwidget |

---

## 二、C++ 类/方法调用频率（全部 DTK 接口，频次 ≥ 1）

| 排名 | 接口（类::方法/枚举） | 频次 | 所属模块 |
|------|---------------------|------|---------|
| 1 | DGuiApplicationHelper::instance | 580 | dtkgui |
| 2 | DFontSizeManager::instance | 522 | dtkgui |
| 3 | DFontSizeManager::T | 462 | dtkgui |
| 4 | DGuiApplicationHelper::ColorType | 279 | dtkgui |
| 5 | DApplication::translate | 187 | dtkwidget |
| 6 | DGuiApplicationHelper::LightType | 176 | dtkgui |
| 7 | DGuiApplicationHelper::themeTypeChanged | 165 | dtkgui |
| 8 | DConfig::create | 146 | dtkcore |
| 9 | DPalette::Text | 138 | dtkgui |
| 10 | DGuiApplicationHelper::DarkType | 107 | dtkgui |
| 11 | DApplicationHelper::instance | 105 | dtkgui |
| 12 | DPaletteHelper::instance | 92 | dtkgui |
| 13 | DFontSizeManager::SizeType | 80 | dtkgui |
| 14 | DConfig::valueChanged | 74 | dtkcore |
| 15 | DPalette::TextTips | 69 | dtkgui |
| 16 | DWindowManagerHelper::instance | 66 | dtkgui |
| 17 | DPalette::Active | 64 | dtkgui |
| 18 | DPalette::TextTitle | 63 | dtkgui |
| 19 | DPalette::ColorGroup | 58 | dtkgui |
| 20 | DPushButton::clicked | 57 | dtkwidget |
| 21 | DSysInfo::uosEditionType | 56 | dtkcore |
| 22 | DSizeModeHelper::element | 56 | dtkgui |
| 23 | DHiDPIHelper::loadNxPixmap | 50 | dtkgui |
| 24 | DIconButton::clicked | 49 | dtkgui |
| 25 | DLogManager::registerConsoleAppender | 47 | dtkcore |
| 26 | DPalette::Inactive | 45 | dtkgui |
| 27 | DDesktopServices::SystemSoundEffect | 45 | dtkcore |
| 28 | DPalette::Base | 44 | dtkgui |
| 29 | DStyle::PM_FrameRadius | 40 | dtkwidget |
| 30 | DLogManager::registerFileAppender | 39 | dtkcore |
| 31 | DPalette::ItemBackground | 38 | dtkgui |
| 32 | DGuiApplicationHelper::generatePaletteColor | 35 | dtkgui |
| 33 | DApplication::activeWindow | 34 | dtkwidget |
| 34 | DStyle::State_Enabled | 33 | dtkwidget |
| 35 | DApplication::style | 33 | dtkwidget |
| 36 | DSysInfo::majorVersion | 31 | dtkcore |
| 37 | DMessageManager::instance | 31 | dtkcore |
| 38 | DSysInfo::UosEdition | 30 | dtkcore |
| 39 | DSysInfo::deepinType | 30 | dtkcore |
| 40 | DDialog::ButtonRecommend | 30 | dtkwidget |
| 41 | DDciIcon::fromTheme | 30 | dtkgui |
| 42 | DApplication::font | 28 | dtkwidget |
| 43 | DApplicationHelper::ColorType | 27 | dtkgui |
| 44 | DGuiApplicationHelper::sizeModeChanged | 26 | dtkgui |
| 45 | DPalette::ColorType | 25 | dtkgui |
| 46 | DLogManager::registerJournalAppender | 25 | dtkcore |
| 47 | DSysInfo::uosType | 24 | dtkcore |
| 48 | DSysInfo::minorVersion | 24 | dtkcore |
| 49 | DDialog::ButtonNormal | 24 | dtkwidget |
| 50 | DWindowManagerHelper::MotifFunctions | 23 | dtkgui |
| 51 | DPalette::Window | 23 | dtkgui |
| 52 | DGuiApplicationHelper::testAttribute | 23 | dtkgui |
| 53 | DDialog::exec | 22 | dtkwidget |
| 54 | DSysInfo::DeepinType | 21 | dtkcore |
| 55 | DPalette::ToolTipText | 21 | dtkgui |
| 56 | DGuiApplicationHelper::IsWaylandPlatform | 21 | dtkgui |
| 57 | DGuiApplicationHelper::adjustColor | 21 | dtkgui |
| 58 | DDialog::ButtonWarning | 21 | dtkwidget |
| 59 | DCommandLinkButton::clicked | 21 | dtkwidget |
| 60 | DApplicationHelper::themeTypeChanged | 21 | dtkgui |
| 61 | DSysInfo::UosServer | 20 | dtkcore |
| 62 | DPalette::FrameBorder | 20 | dtkgui |
| 63 | DConfig::kSearchCfgPath | 20 | dtkcore |
| 64 | DApplication::instance | 20 | dtkwidget |
| 65 | DApplication::fontChanged | 20 | dtkwidget |
| 66 | DSysInfo::uosEditionName | 19 | dtkcore |
| 67 | DPasswordEdit::textChanged | 19 | dtkwidget |
| 68 | DPalette::Button | 19 | dtkgui |
| 69 | DDialog::buttonClicked | 19 | dtkwidget |
| 70 | DSettingsOption::value | 18 | dtkcore |
| 71 | DIcon::loadNxPixmap | 18 | dtkgui |
| 72 | DApplicationHelper::DarkType | 18 | dtkgui |
| 73 | DWidget::paintEvent | 17 | dtkwidget |
| 74 | DSysInfo::UosType | 17 | dtkcore |
| 75 | DSysInfo::UosCommunity | 17 | dtkcore |
| 76 | DPalette::TextWarning | 17 | dtkgui |
| 77 | DToolTip::ShowWhenElided | 16 | dtkwidget |
| 78 | DToolTip::setToolTipShowMode | 16 | dtkwidget |
| 79 | DSuggestButton::clicked | 16 | dtkwidget |
| 80 | DPalette::WindowText | 16 | dtkgui |
| 81 | DPalette::Highlight | 16 | dtkgui |
| 82 | DPalette::AlternateBase | 16 | dtkgui |
| 83 | DGuiApplicationHelper::setAttribute | 16 | dtkgui |
| 84 | DDesktopServices::playSystemSoundEffect | 16 | dtkcore |
| 85 | DApplicationHelper::LightType | 16 | dtkgui |
| 86 | DWindowManagerHelper::FUNC_CLOSE | 15 | dtkgui |
| 87 | DListView::clicked | 15 | dtkwidget |
| 88 | DUtil::DNotifySender | 14 | dtkcore |
| 89 | DStyle::StandardPixmap | 14 | dtkwidget |
| 90 | DPalette::Disabled | 14 | dtkgui |
| 91 | DDialog::Accepted | 14 | dtkwidget |
| 92 | DSysInfo::UosProfessional | 13 | dtkcore |
| 93 | DSysInfo::isCommunityEdition | 13 | dtkcore |
| 94 | DStyle::pixelMetric | 13 | dtkwidget |
| 95 | DPalette::ColorRole | 13 | dtkgui |
| 96 | DPalette::ButtonText | 13 | dtkgui |
| 97 | DDialog::showEvent | 13 | dtkwidget |
| 98 | DAccessibilityChecker::FullFormat | 13 | dtkcore |
| 99 | DSysInfo::isDeepin | 12 | dtkcore |
| 100 | DSysInfo::DeepinServer | 12 | dtkcore |
| 101 | DStyle::PM_ContentsMargins | 12 | dtkwidget |
| 102 | DStyledItemDelegate::BackgroundType | 12 | dtkwidget |
| 103 | DSlider::valueChanged | 12 | dtkwidget |
| 104 | DPalette::Light | 12 | dtkgui |
| 105 | DLineEdit::textChanged | 12 | dtkwidget |
| 106 | DIconTheme::findQIcon | 12 | dtkgui |
| 107 | DFileDragClient::checkMimeData | 12 | dtkgui |
| 108 | DDciIcon::Light | 12 | dtkgui |
| 109 | DBlurEffectWidget::GaussianBlur | 12 | dtkwidget |
| 110 | DWindowManagerHelper::setMotifFunctions | 11 | dtkgui |
| 111 | DWindowManagerHelper::hasCompositeChanged | 11 | dtkgui |
| 112 | DWidget::enterEvent | 11 | dtkwidget |
| 113 | DStyle::State_MouseOver | 11 | dtkwidget |
| 114 | DSettingsOption::valueChanged | 11 | dtkcore |
| 115 | DPalette::NoType | 11 | dtkgui |
| 116 | DPalette::Dark | 11 | dtkgui |
| 117 | DGuiApplicationHelper::UseInactiveColorGroup | 11 | dtkgui |
| 118 | DDialog::ButtonType | 11 | dtkwidget |
| 119 | DDciIcon::Dark | 11 | dtkgui |
| 120 | DUtil::escapeToObjectPath | 10 | dtkcore |
| 121 | DSysInfo::cpuModelName | 10 | dtkcore |
| 122 | DGuiApplicationHelper::themeType | 10 | dtkgui |
| 123 | DBlurEffectWidget::hideEvent | 10 | dtkwidget |
| 124 | DWidget::leaveEvent | 9 | dtkwidget |
| 125 | DUtil::unescapeFromObjectPath | 9 | dtkcore |
| 126 | DSettings::fromJsonFile | 9 | dtkcore |
| 127 | DPalette::PlaceholderText | 9 | dtkgui |
| 128 | DO:: | 9 | other |
| 129 | DMainWindow::closeEvent | 9 | dtkwidget |
| 130 | DLogManager::getlogFilePath | 9 | dtkcore |
| 131 | DListView::mousePressEvent | 9 | dtkwidget |
| 132 | DDialog:: | 9 | dtkwidget |
| 133 | DBlurEffectWidget::showEvent | 9 | dtkwidget |
| 134 | DBlurEffectWidget::BehindWindowBlend | 9 | dtkwidget |
| 135 | DWidget::resizeEvent | 8 | dtkwidget |
| 136 | DWidget::keyPressEvent | 8 | dtkwidget |
| 137 | DWidget::focusOutEvent | 8 | dtkwidget |
| 138 | DToolButton::clicked | 8 | dtkwidget |
| 139 | DSysInfo::distributionOrgLogo | 8 | dtkcore |
| 140 | DSysInfo::DeepinDesktop | 8 | dtkcore |
| 141 | DStyle::SP_ArrowEnter | 8 | dtkwidget |
| 142 | DSlider::LeftIcon | 8 | dtkwidget |
| 143 | DSettingsOption::setValue | 8 | dtkcore |
| 144 | DPalette::Background | 8 | dtkgui |
| 145 | DListView::moveCursor | 8 | dtkwidget |
| 146 | DListView::mouseMoveEvent | 8 | dtkwidget |
| 147 | DLabel::paintEvent | 8 | dtkwidget |
| 148 | DDialog::closeEvent | 8 | dtkwidget |
| 149 | DDesktopServices::showFolder | 8 | dtkcore |
| 150 | DDesktopServices::showFileItem | 8 | dtkcore |
| 151 | DConfig::kEnableFullTextSearch | 8 | dtkcore |
| 152 | DApplication::clipboard | 8 | dtkwidget |
| 153 | DSysInfo::UosHome | 7 | dtkcore |
| 154 | DStyle::PixelMetric | 7 | dtkwidget |
| 155 | DStyledItemDelegate::paint | 7 | dtkwidget |
| 156 | DHeaderView::Interactive | 7 | dtkwidget |
| 157 | DGuiApplicationHelper::loadTranslator | 7 | dtkgui |
| 158 | DFrame::mousePressEvent | 7 | dtkgui |
| 159 | DFileDragClient::setTargetUrl | 7 | dtkgui |
| 160 | DConfig::kEnableFileIndexSearch | 7 | dtkcore |
| 161 | DButtonBoxButton::clicked | 7 | dtkwidget |
| 162 | DBlurEffectWidget::paintEvent | 7 | dtkwidget |
| 163 | DBlurEffectWidget::eventFilter | 7 | dtkwidget |
| 164 | DArrowRectangle::show | 7 | dtkwidget |
| 165 | DArrowRectangle::ArrowTop | 7 | dtkwidget |
| 166 | DApplication::globalApplication | 7 | dtkwidget |
| 167 | DWidget::focusInEvent | 6 | dtkwidget |
| 168 | DSysInfo::productVersion | 6 | dtkcore |
| 169 | DSysInfo::DeepinProfessional | 6 | dtkcore |
| 170 | DStyle::State_Selected | 6 | dtkwidget |
| 171 | DStyle::standardIcon | 6 | dtkwidget |
| 172 | DStyle:: | 6 | dtkwidget |
| 173 | DSlider::RightIcon | 6 | dtkwidget |
| 174 | DSettings::valueChanged | 6 | dtkcore |
| 175 | DPalette::ObviousBackground | 6 | dtkgui |
| 176 | DPalette::BrightText | 6 | dtkgui |
| 177 | DLogManager::setLogFormat | 6 | dtkcore |
| 178 | DListView::setSelectionMode | 6 | dtkwidget |
| 179 | DListView::keyPressEvent | 6 | dtkwidget |
| 180 | DListView::indexAt | 6 | dtkwidget |
| 181 | DListView::currentChanged | 6 | dtkwidget |
| 182 | DLineEdit::focusChanged | 6 | dtkwidget |
| 183 | DGuiApplicationHelper::UnknownType | 6 | dtkgui |
| 184 | DGuiApplicationHelper::setSingleInstance | 6 | dtkgui |
| 185 | DDesktopServices::SSE_Notifications | 6 | dtkcore |
| 186 | DDciIconPreview::updatePixmap | 6 | dtkgui |
| 187 | DConfig::kEnableSemanticSearch | 6 | dtkcore |
| 188 | DConfig::kEnableOcrTextSearch | 6 | dtkcore |
| 189 | DButtonBox::buttonClicked | 6 | dtkwidget |
| 190 | DBlurEffectWidget::LightColor | 6 | dtkwidget |
| 191 | DApplication::UserScope | 6 | dtkwidget |
| 192 | DApplication::buildVersion | 6 | dtkwidget |
| 193 | DTreeView::paintEvent | 5 | dtkwidget |
| 194 | DTextEncoding::detectFileEncoding | 5 | dtkwidget |
| 195 | DTableView::paintEvent | 5 | dtkwidget |
| 196 | DSysInfo::UosEuler | 5 | dtkcore |
| 197 | DSysInfo::ProductType | 5 | dtkcore |
| 198 | DStyle::setFrameRadius | 5 | dtkwidget |
| 199 | DStyledItemDelegate::RoundedBackground | 5 | dtkwidget |
| 200 | DStandardPaths::standardLocations | 5 | dtkcore |
| 201 | DSlider::slider | 5 | dtkwidget |
| 202 | DSGApplication::getId | 5 | dtkcore |
| 203 | DRegionMonitor::Original | 5 | dtkcore |
| 204 | DPalette::Current | 5 | dtkgui |
| 205 | DMainWindow::resizeEvent | 5 | dtkwidget |
| 206 | DLogManager::setlogFilePath | 5 | dtkcore |
| 207 | DListView::setModel | 5 | dtkwidget |
| 208 | DLineEdit::textEdited | 5 | dtkwidget |
| 209 | DHeaderView::paintEvent | 5 | dtkwidget |
| 210 | DGuiApplicationHelper::toColorType | 5 | dtkgui |
| 211 | DFrame::paintEvent | 5 | dtkgui |
| 212 | DFileChooserEdit::fileChoosed | 5 | dtkwidget |
| 213 | DDciIcon::Theme | 5 | dtkgui |
| 214 | DCheckBox::stateChanged | 5 | dtkwidget |
| 215 | DCheckBox::clicked | 5 | dtkwidget |
| 216 | DBlurEffectWidget::resizeEvent | 5 | dtkwidget |
| 217 | DBlurEffectWidget::InWindowBlend | 5 | dtkwidget |
| 218 | DBlurEffectWidget::InWidgetBlend | 5 | dtkwidget |
| 219 | DBlurEffectWidget::enterEvent | 5 | dtkwidget |
| 220 | DApplication::libraryPaths | 5 | dtkwidget |
| 221 | DUtil::getAppIdFromAbsolutePath | 4 | dtkcore |
| 222 | DToolButton::mouseReleaseEvent | 4 | dtkwidget |
| 223 | DToolButton::mousePressEvent | 4 | dtkwidget |
| 224 | DToolButton::leaveEvent | 4 | dtkwidget |
| 225 | DToolButton::event | 4 | dtkwidget |
| 226 | DToolButton::enterEvent | 4 | dtkwidget |
| 227 | DTabBar::eventFilter | 4 | dtkwidget |
| 228 | DSysInfo::UosEducation | 4 | dtkcore |
| 229 | DSysInfo::productTypeString | 4 | dtkcore |
| 230 | DSysInfo::productType | 4 | dtkcore |
| 231 | DSysInfo::Distribution | 4 | dtkcore |
| 232 | DSwitchButton::clicked | 4 | dtkwidget |
| 233 | DSwitchButton::checkedChanged | 4 | dtkwidget |
| 234 | DStyle::SP_LockElement | 4 | dtkwidget |
| 235 | DStyle::PM_ListViewIconSize | 4 | dtkwidget |
| 236 | DStyle::PE_FrameFocusRect | 4 | dtkwidget |
| 237 | DStyledItemDelegate::initStyleOption | 4 | dtkwidget |
| 238 | DStyle::CE_IconButton | 4 | dtkwidget |
| 239 | DSlider::SliderIcons | 4 | dtkwidget |
| 240 | DSlider::setValue | 4 | dtkwidget |
| 241 | DSlider::iconClicked | 4 | dtkwidget |
| 242 | DSettingsWidgetFactory::createStandardItem | 4 | dtkcore |
| 243 | DSearchEdit::textChanged | 4 | dtkwidget |
| 244 | DRegionMonitor::buttonRelease | 4 | dtkcore |
| 245 | DPlatformTheme::iconThemeNameChanged | 4 | dtkgui |
| 246 | DPlatformTheme::activeColorChanged | 4 | dtkgui |
| 247 | DPlainTextEdit::mousePressEvent | 4 | dtkwidget |
| 248 | DPasswordEdit::editingFinished | 4 | dtkwidget |
| 249 | DPalette::HighlightedText | 4 | dtkgui |
| 250 | DMenu::aboutToShow | 4 | dtkwidget |
| 251 | DMenu::aboutToHide | 4 | dtkwidget |
| 252 | DListView::SingleSelection | 4 | dtkwidget |
| 253 | DListView::NoEditTriggers | 4 | dtkwidget |
| 254 | DListView::event | 4 | dtkwidget |
| 255 | DLineEdit::returnPressed | 4 | dtkwidget |
| 256 | DLabel::enterEvent | 4 | dtkwidget |
| 257 | DIconTheme::setDciThemeSearchPaths | 4 | dtkgui |
| 258 | DIconTheme::dciThemeSearchPaths | 4 | dtkgui |
| 259 | DGuiApplicationHelper::UserScope | 4 | dtkgui |
| 260 | DGuiApplicationHelper::newProcessInstance | 4 | dtkgui |
| 261 | DGuiApplicationHelper::isSpecialEffectsEnvironment | 4 | dtkgui |
| 262 | DGuiApplicationHelper::ColorCompositing | 4 | dtkgui |
| 263 | DDialog::keyPressEvent | 4 | dtkwidget |
| 264 | DDialog::closed | 4 | dtkwidget |
| 265 | DDesktopServices::SSE_WakeUp | 4 | dtkcore |
| 266 | DDesktopServices::SSE_Error | 4 | dtkcore |
| 267 | DDesktopServices::SSE_EmptyTrash | 4 | dtkcore |
| 268 | DDE::background | 4 | other |
| 269 | DDciIcon::Mode | 4 | dtkgui |
| 270 | DDciIcon::isNull | 4 | dtkgui |
| 271 | DCCLocale::languageAndRegionName | 4 | other |
| 272 | DBlurEffectWidget::leaveEvent | 4 | dtkwidget |
| 273 | DBlurEffectWidget::AutoColor | 4 | dtkwidget |
| 274 | DArrowRectangle::setContent | 4 | dtkwidget |
| 275 | DApplication::setAttribute | 4 | dtkwidget |
| 276 | DApplication::iconThemeChanged | 4 | dtkwidget |
| 277 | DApplication::applicationState | 4 | dtkwidget |
| 278 | DWidget::showEvent | 3 | dtkwidget |
| 279 | DWidget::mouseReleaseEvent | 3 | dtkwidget |
| 280 | DWidget::mousePressEvent | 3 | dtkwidget |
| 281 | DTreeView::resizeEvent | 3 | dtkwidget |
| 282 | DTreeView::dropEvent | 3 | dtkwidget |
| 283 | DToolButton::mouseMoveEvent | 3 | dtkwidget |
| 284 | DTitlebar::setFixedWidth | 3 | dtkwidget |
| 285 | DTextEncoding::convertTextEncodingEx | 3 | dtkwidget |
| 286 | DSysInfo::uosSystemName | 3 | dtkcore |
| 287 | DSysInfo::uosProductTypeName | 3 | dtkcore |
| 288 | DSysInfo::OrgType | 3 | dtkcore |
| 289 | DSysInfo::memoryTotalSize | 3 | dtkcore |
| 290 | DSysInfo::LogoType | 3 | dtkcore |
| 291 | DSwitchButton::toggled | 3 | dtkwidget |
| 292 | DSuggestButton::animateClick | 3 | dtkwidget |
| 293 | DStyle::State_Sunken | 3 | dtkwidget |
| 294 | DStyle::SP_MarkElement | 3 | dtkwidget |
| 295 | DStyle::SP_DeleteButton | 3 | dtkwidget |
| 296 | DStyle::SP_CloseButton | 3 | dtkwidget |
| 297 | DStyle::SP_AddButton | 3 | dtkwidget |
| 298 | DStyle::PE_ItemBackground | 3 | dtkwidget |
| 299 | DStyle::PE_IndicatorArrowUp | 3 | dtkwidget |
| 300 | DStyle::PE_IndicatorArrowDown | 3 | dtkwidget |
| 301 | DStyleOptionBackgroundGroup::ItemBackgroundPosition | 3 | dtkgui |
| 302 | DStyledItemDelegate::sizeHint | 3 | dtkwidget |
| 303 | DStandardPaths::writableLocation | 3 | dtkcore |
| 304 | DSlider::sliderPressed | 3 | dtkwidget |
| 305 | DSGApplication::id | 3 | dtkcore |
| 306 | DSettingsWidgetFactory::WidgetCreateHandler | 3 | dtkcore |
| 307 | DRegionMonitor::buttonPress | 3 | dtkcore |
| 308 | DRecentManager::addItem | 3 | dtkcore |
| 309 | DPlatformWindowHandle::windowRadiusChanged | 3 | dtkgui |
| 310 | DPlainTextEdit::mouseReleaseEvent | 3 | dtkwidget |
| 311 | DPlainTextEdit::mouseMoveEvent | 3 | dtkwidget |
| 312 | DPasswordEdit::textEdited | 3 | dtkwidget |
| 313 | DMenu::exec | 3 | dtkwidget |
| 314 | DListView::visualRect | 3 | dtkwidget |
| 315 | DListView::updateGeometries | 3 | dtkwidget |
| 316 | DListView::eventFilter | 3 | dtkwidget |
| 317 | DListView::edit | 3 | dtkwidget |
| 318 | DLineEdit::editingFinished | 3 | dtkwidget |
| 319 | DLabel::linkActivated | 3 | dtkwidget |
| 320 | DGuiApplicationHelper::setUseInactiveColorGroup | 3 | dtkgui |
| 321 | DGuiApplicationHelper::setSingleInstanceInterval | 3 | dtkgui |
| 322 | DFrame::Shape | 3 | dtkgui |
| 323 | DFrame::mouseReleaseEvent | 3 | dtkgui |
| 324 | DFrame::mouseMoveEvent | 3 | dtkgui |
| 325 | DFrame::eventFilter | 3 | dtkgui |
| 326 | DFontSizeManager::bind | 3 | dtkgui |
| 327 | DFontSizeManager:: | 3 | dtkgui |
| 328 | DFileSystemWatcher:: | 3 | dtkcore |
| 329 | DFileChooserEdit::textChanged | 3 | dtkwidget |
| 330 | DFileChooserEdit::dialogOpened | 3 | dtkwidget |
| 331 | DDialog::eventFilter | 3 | dtkwidget |
| 332 | DDialogCloseButton::clicked | 3 | dtkwidget |
| 333 | DDesktopServices::SSE_SendFileComplete | 3 | dtkcore |
| 334 | DDesktopServices::SSE_DeviceRemoved | 3 | dtkcore |
| 335 | DDesktopServices::SSE_DeviceAdded | 3 | dtkcore |
| 336 | DDEindicatorProtocol::registedItemChanged | 3 | other |
| 337 | DDciIcon::Normal | 3 | dtkgui |
| 338 | DCrumbEdit::clear | 3 | dtkwidget |
| 339 | DCrumbEdit:: | 3 | dtkwidget |
| 340 | DConfig::createGeneric | 3 | dtkcore |
| 341 | DCCLocale::dialectNames | 3 | other |
| 342 | DButtonBoxButton::toggled | 3 | dtkwidget |
| 343 | DButtonBox::buttonToggled | 3 | dtkwidget |
| 344 | DBlurEffectWidget::hide | 3 | dtkwidget |
| 345 | DArrowRectangle::showEvent | 3 | dtkwidget |
| 346 | DArrowRectangle::hide | 3 | dtkwidget |
| 347 | DArrowRectangle::enterEvent | 3 | dtkwidget |
| 348 | DApplication::notify | 3 | dtkwidget |
| 349 | DApplicationHelper::UnknownType | 3 | dtkgui |
| 350 | DAnchorsBase::setAnchor | 3 | dtkcore |
| 351 | DAnchorsBase::clearAnchors | 3 | dtkcore |
| 352 | DWindowManagerHelper::hasBlurWindowChanged | 2 | dtkgui |
| 353 | DWidget::startCount | 2 | dtkwidget |
| 354 | DWidget::setEnabled | 2 | dtkwidget |
| 355 | DWidget::onVerificationCodeBtnClicked | 2 | dtkwidget |
| 356 | DWidget::onVerficationCodeCountReplied | 2 | dtkwidget |
| 357 | DWidget::onRequestVerifyVerficationCodeReplied | 2 | dtkwidget |
| 358 | DWidget::onRequestVerficationCodeReplied | 2 | dtkwidget |
| 359 | DWidget::onPhoneEmailLineEditFocusChanged | 2 | dtkwidget |
| 360 | DWidget::onBindCheckUbidReplied | 2 | dtkwidget |
| 361 | DWidget::onBindCheckReplied | 2 | dtkwidget |
| 362 | DWidget::eventFilter | 2 | dtkwidget |
| 363 | DWaterProgress::start | 2 | dtkwidget |
| 364 | DTreeView::viewportEvent | 2 | dtkwidget |
| 365 | DTreeView::sizeHintForColumn | 2 | dtkwidget |
| 366 | DTreeView::setModel | 2 | dtkwidget |
| 367 | DTreeView::selectionChanged | 2 | dtkwidget |
| 368 | DTreeView::keyPressEvent | 2 | dtkwidget |
| 369 | DTreeView::focusInEvent | 2 | dtkwidget |
| 370 | DTreeView::currentChanged | 2 | dtkwidget |
| 371 | DTrashManager::instance | 2 | dtkcore |
| 372 | DToolTip::wrapToolTipText | 2 | dtkwidget |
| 373 | DToolButton::initStyleOption | 2 | dtkwidget |
| 374 | DTitlebar::setTitle | 2 | dtkwidget |
| 375 | DTitlebar::setFont | 2 | dtkwidget |
| 376 | DTextEdit::showEvent | 2 | dtkwidget |
| 377 | DTextEdit::keyPressEvent | 2 | dtkwidget |
| 378 | DTextEdit::focusOutEvent | 2 | dtkwidget |
| 379 | DTextEdit::eventFilter | 2 | dtkwidget |
| 380 | DTableWidget::paintEvent | 2 | dtkwidget |
| 381 | DTableWidget::clear | 2 | dtkwidget |
| 382 | DTableView::NoFrame | 2 | dtkwidget |
| 383 | DSysInfo::UosEnterpriseC | 2 | dtkcore |
| 384 | DSysInfo::UosEnterprise | 2 | dtkcore |
| 385 | DSysInfo::memoryInstalledSize | 2 | dtkcore |
| 386 | DSysInfo::Light | 2 | dtkcore |
| 387 | DSysInfo::DSysInfo | 2 | dtkcore |
| 388 | DSysInfo::DeepinPersonal | 2 | dtkcore |
| 389 | DStyle::SP_SelectElement | 2 | dtkwidget |
| 390 | DStyle::SP_ReduceElement | 2 | dtkwidget |
| 391 | DStyle::SP_ArrowNext | 2 | dtkwidget |
| 392 | DStyle::setFocusRectVisible | 2 | dtkwidget |
| 393 | DStyle::generatedBrush | 2 | dtkwidget |
| 394 | DStyledItemDelegate::editorEvent | 2 | dtkwidget |
| 395 | DStyledItemDelegate::ClipCornerBackground | 2 | dtkwidget |
| 396 | DSlider::sliderMoved | 2 | dtkwidget |
| 397 | DSettingsOption::key | 2 | dtkcore |
| 398 | DSettings::fromJson | 2 | dtkcore |
| 399 | DRegionMonitor::WatchedFlags | 2 | dtkcore |
| 400 | DPushButton::leaveEvent | 2 | dtkwidget |
| 401 | DPushButton::keyPressEvent | 2 | dtkwidget |
| 402 | DPushButton::focusOutEvent | 2 | dtkwidget |
| 403 | DPushButton::focusInEvent | 2 | dtkwidget |
| 404 | DPushButton::enterEvent | 2 | dtkwidget |
| 405 | DPlatformWindowHandle::setDisableWindowOverrideCursor | 2 | dtkgui |
| 406 | DPlatformWindowHandle::enableDXcbForWindow | 2 | dtkgui |
| 407 | DPlatformTheme::windowRadiusChanged | 2 | dtkgui |
| 408 | DPlatformTheme::themeNameChanged | 2 | dtkgui |
| 409 | DPlatformTheme::fontPointSizeChanged | 2 | dtkgui |
| 410 | DPlatformTheme::fontNameChanged | 2 | dtkgui |
| 411 | DPlatformTheme::darkActiveColorChanged | 2 | dtkgui |
| 412 | DPasswordEdit::focusChanged | 2 | dtkwidget |
| 413 | DPaletteHelper::palette | 2 | dtkgui |
| 414 | DMainWindow::showEvent | 2 | dtkwidget |
| 415 | DMainWindow::keyPressEvent | 2 | dtkwidget |
| 416 | DMainWindow::eventFilter | 2 | dtkwidget |
| 417 | DMainWindow::event | 2 | dtkwidget |
| 418 | DListView::wheelEvent | 2 | dtkwidget |
| 419 | DListView::showEvent | 2 | dtkwidget |
| 420 | DListView::setCurrentIndex | 2 | dtkwidget |
| 421 | DListView::rowCountChanged | 2 | dtkwidget |
| 422 | DListView::pressed | 2 | dtkwidget |
| 423 | DListView::paintEvent | 2 | dtkwidget |
| 424 | DListView::MultiSelection | 2 | dtkwidget |
| 425 | DListView::mouseReleaseEvent | 2 | dtkwidget |
| 426 | DListView::hideEvent | 2 | dtkwidget |
| 427 | DListView::dropEvent | 2 | dtkwidget |
| 428 | DListView::dragLeaveEvent | 2 | dtkwidget |
| 429 | DListView::doubleClicked | 2 | dtkwidget |
| 430 | DListView::clearSelection | 2 | dtkwidget |
| 431 | DLabel::setPixmap | 2 | dtkwidget |
| 432 | DLabel::eventFilter | 2 | dtkwidget |
| 433 | DIconTheme::IgnoreBuiltinIcons | 2 | dtkgui |
| 434 | DIconButton::initStyleOption | 2 | dtkgui |
| 435 | DIconButton::CustomDIconButton | 2 | dtkgui |
| 436 | DHeaderView::focusInEvent | 2 | dtkwidget |
| 437 | DGuiApplicationHelper::standardPalette | 2 | dtkgui |
| 438 | DGuiApplicationHelper::SizeMode | 2 | dtkgui |
| 439 | DGuiApplicationHelper::isXWindowPlatform | 2 | dtkgui |
| 440 | DGuiApplicationHelper::fontChanged | 2 | dtkgui |
| 441 | DGuiApplicationHelper::applicationPaletteChanged | 2 | dtkgui |
| 442 | DFrame::resizeEvent | 2 | dtkgui |
| 443 | DFrame::NoFrame | 2 | dtkgui |
| 444 | DForeignWindow::fromWinId | 2 | dtkgui |
| 445 | DFileDragClient::stateChanged | 2 | dtkgui |
| 446 | DFileDragClient::serverDestroyed | 2 | dtkgui |
| 447 | DFileDragClient::destroyed | 2 | dtkgui |
| 448 | DFileDragClient::deleteLater | 2 | dtkgui |
| 449 | DFileDialog::getOpenFileName | 2 | dtkwidget |
| 450 | DFileDialog::getExistingDirectory | 2 | dtkwidget |
| 451 | DFileDialog::ExistingFiles | 2 | dtkwidget |
| 452 | DDialog::mousePressEvent | 2 | dtkwidget |
| 453 | DDialog::changeEvent | 2 | dtkwidget |
| 454 | DDesktopServices::SSE_VolumeChange | 2 | dtkcore |
| 455 | DDesktopServices::SSE_Shutdown | 2 | dtkcore |
| 456 | DDesktopServices::SSE_Screenshot | 2 | dtkcore |
| 457 | DDesktopServices::SSE_Logout | 2 | dtkcore |
| 458 | DDesktopServices::SSE_BootUp | 2 | dtkcore |
| 459 | DDesktopServices::SEE_Screenshot | 2 | dtkcore |
| 460 | DDesktopEntry::NoError | 2 | dtkcore |
| 461 | DDE::onAppearanceValueChanged | 2 | other |
| 462 | DDE::getBackgroundFromDDE | 2 | other |
| 463 | DDciIcon::DontFallbackMode | 2 | dtkgui |
| 464 | DCrumbEdit::insertCrumb | 2 | dtkwidget |
| 465 | DCrumbEdit::crumbListChanged | 2 | dtkwidget |
| 466 | DCrumbEdit::crumbList | 2 | dtkwidget |
| 467 | DConfig::kSearchAuthHintDone | 2 | dtkcore |
| 468 | DConfig::kNextShutdownTime | 2 | dtkcore |
| 469 | DConfig::kHighPerformanceEnabled | 2 | dtkcore |
| 470 | DColoredProgressBar::setValue | 2 | dtkwidget |
| 471 | DBlurEffectWidget::mouseReleaseEvent | 2 | dtkwidget |
| 472 | DBlurEffectWidget::maskAlphaChanged | 2 | dtkwidget |
| 473 | DBlurEffectWidget::keyPressEvent | 2 | dtkwidget |
| 474 | DArrowLineDrawer::closeEvent | 2 | dtkwidget |
| 475 | DApplication::runtimeDtkVersion | 2 | dtkwidget |
| 476 | DApplication::quit | 2 | dtkwidget |
| 477 | DApplication::loadDXcbPlugin | 2 | dtkwidget |
| 478 | DApplicationHelper::fontChanged | 2 | dtkgui |
| 479 | DApplication::event | 2 | dtkwidget |
| 480 | DAccessibilityChecker::isIgnore | 2 | dtkcore |
| 481 | DWindowManagerHelper::WMName | 1 | dtkgui |
| 482 | DWindowManagerHelper::KWinWM | 1 | dtkgui |
| 483 | DWidget::UnionIDWidget | 1 | dtkwidget |
| 484 | DWidget::UNION_ID_ERROR_TYPE | 1 | dtkwidget |
| 485 | DWidget::setIconPath | 1 | dtkwidget |
| 486 | DWidget::requestVerifyVerficationCode | 1 | dtkwidget |
| 487 | DWidget::requestAsyncVerficationCode | 1 | dtkwidget |
| 488 | DWidget::requestAsyncBindCheck | 1 | dtkwidget |
| 489 | DWidget::parseError | 1 | dtkwidget |
| 490 | DWidget::pageChanged | 1 | dtkwidget |
| 491 | DWidget::onResetPasswordBtnClicked | 1 | dtkwidget |
| 492 | DWidget::mouseMoveEvent | 1 | dtkwidget |
| 493 | DWidget::mouseDoubleClickEvent | 1 | dtkwidget |
| 494 | DWidget::loadPage | 1 | dtkwidget |
| 495 | DWidget::keyReleaseEvent | 1 | dtkwidget |
| 496 | DWidget::isContentEmpty | 1 | dtkwidget |
| 497 | DWidget::initWidget | 1 | dtkwidget |
| 498 | DWidget::initData | 1 | dtkwidget |
| 499 | DWidget::getErrorTips | 1 | dtkwidget |
| 500 | DWidget::event | 1 | dtkwidget |
| 501 | DWidget::checkPhoneEmailFormat | 1 | dtkwidget |
| 502 | DUtil::TimerSingleShot | 1 | dtkcore |
| 503 | DTreeView::startDrag | 1 | dtkwidget |
| 504 | DTreeView::showEvent | 1 | dtkwidget |
| 505 | DTreeView::mouseReleaseEvent | 1 | dtkwidget |
| 506 | DTreeView::mousePressEvent | 1 | dtkwidget |
| 507 | DTreeView::indexAt | 1 | dtkwidget |
| 508 | DTreeView::dragMoveEvent | 1 | dtkwidget |
| 509 | DTreeView::dragEnterEvent | 1 | dtkwidget |
| 510 | DTreeView::doubleClicked | 1 | dtkwidget |
| 511 | DTreeView::clicked | 1 | dtkwidget |
| 512 | DToolButton::resizeEvent | 1 | dtkwidget |
| 513 | DToolButton::paintEvent | 1 | dtkwidget |
| 514 | DToolButton::moveEvent | 1 | dtkwidget |
| 515 | DToolButton::CustomDToolButton | 1 | dtkwidget |
| 516 | DTipLabel::linkActivated | 1 | dtkwidget |
| 517 | DTextEncoding::convertTextEncoding | 1 | dtkwidget |
| 518 | DTextEdit::textChanged | 1 | dtkwidget |
| 519 | DTextBrowser::paintEvent | 1 | dtkwidget |
| 520 | DTextBrowser::keyPressEvent | 1 | dtkwidget |
| 521 | DTextBrowser::focusOutEvent | 1 | dtkwidget |
| 522 | DTableWidget::wheelEvent | 1 | dtkwidget |
| 523 | DTableWidget::setItem | 1 | dtkwidget |
| 524 | DTableWidget::resizeEvent | 1 | dtkwidget |
| 525 | DTableWidget::mousePressEvent | 1 | dtkwidget |
| 526 | DTableWidget::mouseMoveEvent | 1 | dtkwidget |
| 527 | DTableWidget::leaveEvent | 1 | dtkwidget |
| 528 | DTabBar::tabSizeHint | 1 | dtkwidget |
| 529 | DTabBar::tabMoved | 1 | dtkwidget |
| 530 | DTabBar::tabDroped | 1 | dtkwidget |
| 531 | DTabBar::resizeEvent | 1 | dtkwidget |
| 532 | DTabBar::removeTab | 1 | dtkwidget |
| 533 | DTabBar::mousePressEvent | 1 | dtkwidget |
| 534 | DTabBar::createDragPixmapFromTab | 1 | dtkwidget |
| 535 | DTabBar::count | 1 | dtkwidget |
| 536 | DSysInfo::UosMilitary | 1 | dtkcore |
| 537 | DSysInfo::UosEditionUnknown | 1 | dtkcore |
| 538 | DSysInfo::udpateVersion | 1 | dtkcore |
| 539 | DSysInfo::Transparent | 1 | dtkcore |
| 540 | DSysInfo::spVersion | 1 | dtkcore |
| 541 | DSysInfo::Normal | 1 | dtkcore |
| 542 | DSysInfo::isDDE | 1 | dtkcore |
| 543 | DSysInfo::computerName | 1 | dtkcore |
| 544 | DSysInfo::buildVersion | 1 | dtkcore |
| 545 | DSwitchButton::setEnabled | 1 | dtkwidget |
| 546 | DSwitchButton::pressed | 1 | dtkwidget |
| 547 | DSuggestButton::released | 1 | dtkwidget |
| 548 | DSuggestButton::pressed | 1 | dtkwidget |
| 549 | DSuggestButton::isEnabled | 1 | dtkwidget |
| 550 | DStyle::toDciIconMode | 1 | dtkwidget |
| 551 | DStyle::SubElement | 1 | dtkwidget |
| 552 | DStyle::State_On | 1 | dtkwidget |
| 553 | DStyle::SP_IncreaseElement | 1 | dtkwidget |
| 554 | DStyle::SP_ArrowLeave | 1 | dtkwidget |
| 555 | DStyle::PM_FocusBorderWidth | 1 | dtkwidget |
| 556 | DStyle::PE_IndicatorItemViewItemCheck | 1 | dtkwidget |
| 557 | DStyleOptionButton::TitleBarButton | 1 | dtkgui |
| 558 | DStyledItemDelegate::updateEditorGeometry | 1 | dtkwidget |
| 559 | DStyledItemDelegate::NoNormalState | 1 | dtkwidget |
| 560 | DStyledItemDelegate::createEditor | 1 | dtkwidget |
| 561 | DStandardPaths::homePath | 1 | dtkcore |
| 562 | DStandardItem::setDciIcon | 1 | dtkwidget |
| 563 | DStandardItem:: | 1 | dtkwidget |
| 564 | DS::signalStatus | 1 | other |
| 565 | DS::save_driver_info | 1 | other |
| 566 | DSplitter::resizeEvent | 1 | dtkwidget |
| 567 | DSplitter::childEvent | 1 | dtkwidget |
| 568 | DSpinner::stop | 1 | dtkwidget |
| 569 | DSpinner::start | 1 | dtkwidget |
| 570 | DSpinBox::valueChanged | 1 | dtkwidget |
| 571 | DSpinBox:: | 1 | dtkwidget |
| 572 | DSlider::sliderReleased | 1 | dtkwidget |
| 573 | DSlider::resizeEvent | 1 | dtkwidget |
| 574 | DSlider::leaveEvent | 1 | dtkwidget |
| 575 | DSlider::enterEvent | 1 | dtkwidget |
| 576 | DSettings::setOption | 1 | dtkcore |
| 577 | DSettingsDialog::showEvent | 1 | dtkcore |
| 578 | DSettingsDialog::finished | 1 | dtkcore |
| 579 | DSettingsDialog::exec | 1 | dtkcore |
| 580 | DSettingsDialog::closeEvent | 1 | dtkcore |
| 581 | DSearchEdit::textEdited | 1 | dtkwidget |
| 582 | DSearchEdit::selectionChanged | 1 | dtkwidget |
| 583 | DSearchEdit::searchAborted | 1 | dtkwidget |
| 584 | DS::doWork | 1 | other |
| 585 | DRegionMonitor::Wheel_Up | 1 | dtkcore |
| 586 | DRegionMonitor::unregisterRegion | 1 | dtkcore |
| 587 | DRegionMonitor::setCoordinateType | 1 | dtkcore |
| 588 | DRegionMonitor::registerRegion | 1 | dtkcore |
| 589 | DRegionMonitor::CoordinateType | 1 | dtkcore |
| 590 | DRegionMonitor:: | 1 | dtkcore |
| 591 | DRecentManager::removeItems | 1 | dtkcore |
| 592 | DPushButton::mouseReleaseEvent | 1 | dtkwidget |
| 593 | DPushButton::mousePressEvent | 1 | dtkwidget |
| 594 | DPushButton::mouseMoveEvent | 1 | dtkwidget |
| 595 | DPushButton::hideEvent | 1 | dtkwidget |
| 596 | DPushButton::eventFilter | 1 | dtkwidget |
| 597 | DPlatformWindowHandle::pluginVersion | 1 | dtkgui |
| 598 | DPlatformWindowHandle::isEnabledDXcb | 1 | dtkgui |
| 599 | DPlatformWindowHandle::EffectType | 1 | dtkgui |
| 600 | DPlatformWindowHandle::EffectScene | 1 | dtkgui |
| 601 | DPlainTextEdit::NoWrap | 1 | dtkwidget |
| 602 | DPlainTextEdit::mouseDoubleClickEvent | 1 | dtkwidget |
| 603 | DPlainTextEdit::keyPressEvent | 1 | dtkwidget |
| 604 | DPlainTextEdit::inputMethodEvent | 1 | dtkwidget |
| 605 | DPlainTextEdit::focusOutEvent | 1 | dtkwidget |
| 606 | DPlainTextEdit::focusInEvent | 1 | dtkwidget |
| 607 | DPalette::TextLively | 1 | dtkgui |
| 608 | DPalette::FrameShadowBorder | 1 | dtkgui |
| 609 | DPalette::Foreground | 1 | dtkgui |
| 610 | DMessageBox::standardIcon | 1 | dtkwidget |
| 611 | DMessageBox::Critical | 1 | dtkwidget |
| 612 | DMenu::triggered | 1 | dtkwidget |
| 613 | DMainWindow::moveEvent | 1 | dtkwidget |
| 614 | DMainWindow::mouseDoubleClickEvent | 1 | dtkwidget |
| 615 | DLogManager::registerLoggingRulesWatcher | 1 | dtkcore |
| 616 | DListView::viewportMargins | 1 | dtkwidget |
| 617 | DListView::verticalOffset | 1 | dtkwidget |
| 618 | DListView::timerEvent | 1 | dtkwidget |
| 619 | DListView::sizeHintForIndex | 1 | dtkwidget |
| 620 | DListView::setRowHidden | 1 | dtkwidget |
| 621 | DListView::setIconSize | 1 | dtkwidget |
| 622 | DListView::scrollTo | 1 | dtkwidget |
| 623 | DListView::ScrollPerPixel | 1 | dtkwidget |
| 624 | DListView::rowsAboutToBeRemoved | 1 | dtkwidget |
| 625 | DListView::resizeEvent | 1 | dtkwidget |
| 626 | DListView::NoState | 1 | dtkwidget |
| 627 | DListView::mouseDoubleClickEvent | 1 | dtkwidget |
| 628 | DListView::leaveEvent | 1 | dtkwidget |
| 629 | DListView::itemDelegate | 1 | dtkwidget |
| 630 | DListView::iconSizeChanged | 1 | dtkwidget |
| 631 | DListView::Free | 1 | dtkwidget |
| 632 | DListView::focusInEvent | 1 | dtkwidget |
| 633 | DListView::Fixed | 1 | dtkwidget |
| 634 | DListView::dragEnterEvent | 1 | dtkwidget |
| 635 | DListView::doItemsLayout | 1 | dtkwidget |
| 636 | DListView::dataChanged | 1 | dtkwidget |
| 637 | DListView::customContextMenuRequested | 1 | dtkwidget |
| 638 | DListView::Batched | 1 | dtkwidget |
| 639 | DListView::Adjust | 1 | dtkwidget |
| 640 | DListView::activated | 1 | dtkwidget |
| 641 | DListView:: | 1 | dtkwidget |
| 642 | DLineEdit::setToolTip | 1 | dtkwidget |
| 643 | DLineEdit::setText | 1 | dtkwidget |
| 644 | DLineEdit::resizeEvent | 1 | dtkwidget |
| 645 | DLineEdit::hasFocus | 1 | dtkwidget |
| 646 | DLineEdit::eventFilter | 1 | dtkwidget |
| 647 | DLabel::setText | 1 | dtkwidget |
| 648 | DLabel::setForegroundRole | 1 | dtkwidget |
| 649 | DLabel::setFixedWidth | 1 | dtkwidget |
| 650 | DLabel::setAlignment | 1 | dtkwidget |
| 651 | DLabel::isVisible | 1 | dtkwidget |
| 652 | DLabel::fontMetrics | 1 | dtkwidget |
| 653 | DLabel::fontInfo | 1 | dtkwidget |
| 654 | DLabel::changeEvent | 1 | dtkwidget |
| 655 | DKeySequenceEdit::editingFinished | 1 | dtkwidget |
| 656 | DIconTheme::DontFallbackToQIconFromTheme | 1 | dtkgui |
| 657 | DIconButton::toggled | 1 | dtkgui |
| 658 | DIconButton::paintEvent | 1 | dtkgui |
| 659 | DIconButtonHoverFilter::staticMetaObject | 1 | dtkgui |
| 660 | DIconButtonHoverFilter::qt_static_metacall | 1 | dtkgui |
| 661 | DIconButtonHoverFilter::qt_metacast | 1 | dtkgui |
| 662 | DIconButtonHoverFilter::qt_metacall | 1 | dtkgui |
| 663 | DIconButtonHoverFilter::metaObject | 1 | dtkgui |
| 664 | DHeaderView::Stretch | 1 | dtkwidget |
| 665 | DHeaderView::ResizeToContents | 1 | dtkwidget |
| 666 | DHeaderView::eventFilter | 1 | dtkwidget |
| 667 | DGuiApplicationHelper::setColorCompositingEnabled | 1 | dtkgui |
| 668 | DGuiApplicationHelper::IsXWindowPlatform | 1 | dtkgui |
| 669 | DGuiApplicationHelper::isTabletEnvironment | 1 | dtkgui |
| 670 | DGuiApplicationHelper::IsDXcbPlatform | 1 | dtkgui |
| 671 | DGuiApplicationHelper::fetchPalette | 1 | dtkgui |
| 672 | DGuiApplicationHelper::DontSaveApplicationTheme | 1 | dtkgui |
| 673 | DGraphicsView::focusOutEvent | 1 | dtkwidget |
| 674 | DFrame::showEvent | 1 | dtkgui |
| 675 | DFrame::focusOutEvent | 1 | dtkgui |
| 676 | DFrame::event | 1 | dtkgui |
| 677 | DFileWatcherManager::fileModified | 1 | dtkcore |
| 678 | DFileWatcherManager::fileAttributeChanged | 1 | dtkcore |
| 679 | DFileSystemWatcher::removePaths | 1 | dtkcore |
| 680 | DFileSystemWatcher::removePath | 1 | dtkcore |
| 681 | DFileSystemWatcher::addPath | 1 | dtkcore |
| 682 | DFileDialog::getSaveFileName | 1 | dtkwidget |
| 683 | DFileDialog::getExistingDirectoryUrl | 1 | dtkwidget |
| 684 | DFileDialog::fileSelected | 1 | dtkwidget |
| 685 | DFileDialog::ExistingFile | 1 | dtkwidget |
| 686 | DFileDialog::exec | 1 | dtkwidget |
| 687 | DFileDialog::Detail | 1 | dtkwidget |
| 688 | DFileDialog::Accepted | 1 | dtkwidget |
| 689 | DFileChooserEdit::CurrentMonitorCenter | 1 | dtkwidget |
| 690 | DDialog::resizeEvent | 1 | dtkwidget |
| 691 | DDialog::reject | 1 | dtkwidget |
| 692 | DDialog::hideEvent | 1 | dtkwidget |
| 693 | DDialog::getButton | 1 | dtkwidget |
| 694 | DDialog::finished | 1 | dtkwidget |
| 695 | DDialog::event | 1 | dtkwidget |
| 696 | DDialog::close | 1 | dtkwidget |
| 697 | DDialog::accept | 1 | dtkwidget |
| 698 | DDesktopServices::SSE_PlugOut | 1 | dtkcore |
| 699 | DDesktopServices::SSE_PlugIn | 1 | dtkcore |
| 700 | DDesktopServices::SSE_LowBattery | 1 | dtkcore |
| 701 | DDE::is_dummy_package | 1 | other |
| 702 | DDEindicatorProtocolHandler::windowId | 1 | other |
| 703 | DDEindicatorProtocolHandler::title | 1 | other |
| 704 | DDEindicatorProtocolHandler::textPropertyChanged | 1 | other |
| 705 | DDEindicatorProtocolHandler::status | 1 | other |
| 706 | DDEindicatorProtocolHandler::setEnabled | 1 | other |
| 707 | DDEindicatorProtocolHandlerPrivate::updateContent | 1 | other |
| 708 | DDEindicatorProtocolHandlerPrivate::propertyChanged | 1 | other |
| 709 | DDEindicatorProtocolHandlerPrivate::initDBus | 1 | other |
| 710 | DDEindicatorProtocolHandlerPrivate::init | 1 | other |
| 711 | DDEindicatorProtocolHandlerPrivate::featData | 1 | other |
| 712 | DDEindicatorProtocolHandler::overlayIcon | 1 | other |
| 713 | DDEindicatorProtocolHandler::id | 1 | other |
| 714 | DDEindicatorProtocolHandler::iconPropertyChanged | 1 | other |
| 715 | DDEindicatorProtocolHandler::icon | 1 | other |
| 716 | DDEindicatorProtocolHandler::eventFilter | 1 | other |
| 717 | DDEindicatorProtocolHandler::enabled | 1 | other |
| 718 | DDEindicatorProtocolHandler::DDEindicatorProtocolHandler | 1 | other |
| 719 | DDEindicatorProtocolHandler::clicked | 1 | other |
| 720 | DDEindicatorProtocolHandler::category | 1 | other |
| 721 | DDEindicatorProtocolHandler::attentionIcon | 1 | other |
| 722 | DDEindicatorProtocolHandler:: | 1 | other |
| 723 | DDEindicatorProtocol::DDEindicatorProtocol | 1 | other |
| 724 | DDEindicatorProtocol:: | 1 | other |
| 725 | DDE::getDefaultBackground | 1 | other |
| 726 | DDE::getBackgroundFromConfig | 1 | other |
| 727 | DDE::BackgroundDDE | 1 | other |
| 728 | DDE:: | 1 | other |
| 729 | DDciIconPreview::updatePixmapImpl | 1 | dtkgui |
| 730 | DDciIconPreview::updateIconMatchedResult | 1 | dtkgui |
| 731 | DDciIconPreview::title | 1 | dtkgui |
| 732 | DDciIconPreview::timerEvent | 1 | dtkgui |
| 733 | DDciIconPreview::statusBarWidget | 1 | dtkgui |
| 734 | DDciIconPreview::setFileUrl | 1 | dtkgui |
| 735 | DDciIconPreviewPlugin::create | 1 | dtkgui |
| 736 | DDciIconPreview::initPreviewWidgets | 1 | dtkgui |
| 737 | DDciIconPreview::initializeSettings | 1 | dtkgui |
| 738 | DDciIconPreview::initialize | 1 | dtkgui |
| 739 | DDciIconPreview::initControlWidgets | 1 | dtkgui |
| 740 | DDciIconPreview::getIconSize | 1 | dtkgui |
| 741 | DDciIconPreview::generateDciIconPalette | 1 | dtkgui |
| 742 | DDciIconPreview::fileUrl | 1 | dtkgui |
| 743 | DDciIconPreview::eventFilter | 1 | dtkgui |
| 744 | DDciIconPreview::DDciIconPreview | 1 | dtkgui |
| 745 | DDciIconPreview::contentWidget | 1 | dtkgui |
| 746 | DDciIconPreview:: | 1 | dtkgui |
| 747 | DDciIcon::pixmap | 1 | dtkgui |
| 748 | DDciIcon::HasPalette | 1 | dtkgui |
| 749 | DCrumbEdit::toPlainText | 1 | dtkwidget |
| 750 | DCrumbEdit::mouseDoubleClickEvent | 1 | dtkwidget |
| 751 | DCrumbEdit::appendCrumb | 1 | dtkwidget |
| 752 | DConfig::value | 1 | dtkcore |
| 753 | DConfig::kSleepLock | 1 | dtkcore |
| 754 | DConfig::kShutdownTime | 1 | dtkcore |
| 755 | DConfig::kShutdownRepetition | 1 | dtkcore |
| 756 | DConfig::kShutdownCountdown | 1 | dtkcore |
| 757 | DConfig::kScreenBlackLock | 1 | dtkcore |
| 758 | DConfig::kScheduledShutdownState | 1 | dtkcore |
| 759 | DConfig::kPowerName | 1 | dtkcore |
| 760 | DConfig::kPercentageAction | 1 | dtkcore |
| 761 | DConfig::kLowPowerNotifyThreshold | 1 | dtkcore |
| 762 | DConfig::kLowPowerNotifyEnable | 1 | dtkcore |
| 763 | DConfig::kLowPowerAction | 1 | dtkcore |
| 764 | DConfig::kLinePowerSleepDelay | 1 | dtkcore |
| 765 | DConfig::kLinePowerScreensaverDelay | 1 | dtkcore |
| 766 | DConfig::kLinePowerScreenBlackDelay | 1 | dtkcore |
| 767 | DConfig::kLinePowerPressPowerButton | 1 | dtkcore |
| 768 | DConfig::kLinePowerLockDelay | 1 | dtkcore |
| 769 | DConfig::kLinePowerLidClosedAction | 1 | dtkcore |
| 770 | DConfig::kCustomShutdownWeekDays | 1 | dtkcore |
| 771 | DConfig::kBatterySleepDelay | 1 | dtkcore |
| 772 | DConfig::kBatteryScreensaverDelay | 1 | dtkcore |
| 773 | DConfig::kBatteryScreenBlackDelay | 1 | dtkcore |
| 774 | DConfig::kBatteryPressPowerButton | 1 | dtkcore |
| 775 | DConfig::kBatteryLockDelay | 1 | dtkcore |
| 776 | DConfig::kBatteryLidClosedAction | 1 | dtkcore |
| 777 | DConfig::kAppId | 1 | dtkcore |
| 778 | DConfig::kAmbientLightAdjustBrightness | 1 | dtkcore |
| 779 | DConfig::deleteLater | 1 | dtkcore |
| 780 | DCommandLinkButton::pressed | 1 | dtkwidget |
| 781 | DCommandLinkButton::paintEvent | 1 | dtkwidget |
| 782 | DCommandLinkButton::eventFilter | 1 | dtkwidget |
| 783 | DCheckBox::checkStateChanged | 1 | dtkwidget |
| 784 | DButtonBox::focusInEvent | 1 | dtkwidget |
| 785 | DBlurEffectWidget::staticMetaObject | 1 | dtkwidget |
| 786 | DBlurEffectWidget::show | 1 | dtkwidget |
| 787 | DBlurEffectWidget::setGeometry | 1 | dtkwidget |
| 788 | DBlurEffectWidget::setBlendMode | 1 | dtkwidget |
| 789 | DBlurEffectWidget::qt_metacast | 1 | dtkwidget |
| 790 | DBlurEffectWidget::qt_metacall | 1 | dtkwidget |
| 791 | DBlurEffectWidget::mousePressEvent | 1 | dtkwidget |
| 792 | DBlurEffectWidget::focusOutEvent | 1 | dtkwidget |
| 793 | DBlurEffectWidget::event | 1 | dtkwidget |
| 794 | DBlurEffectWidget::BlendMode | 1 | dtkwidget |
| 795 | DArrowRectangle::keyPressEvent | 1 | dtkwidget |
| 796 | DArrowRectangle::eventFilter | 1 | dtkwidget |
| 797 | DArrowRectangle::ArrowDirection | 1 | dtkwidget |
| 798 | DArrowRectangle::ArrowBottom | 1 | dtkwidget |
| 799 | DArrowLineDrawer::paintEvent | 1 | dtkwidget |
| 800 | DApplication::setOverrideCursor | 1 | dtkwidget |
| 801 | DApplication::restoreOverrideCursor | 1 | dtkwidget |
| 802 | DApplication::newInstanceStarted | 1 | dtkwidget |
| 803 | DApplication::keyboardModifiers | 1 | dtkwidget |
| 804 | DAnchorsBase::getAnchorBaseByWidget | 1 | dtkcore |

---

## 三、QML 中 DTK 组件使用频率

### 3.1 QML 导入语句

| 导入语句 | 使用次数 |
|---------|---------|
| import org.deepin.dtk 1.0 | 308 |
| import org.deepin.dtk 1.0 as D | 215 |
| import org.deepin.dtk.style 1.0 as DS | 95 |
| import org.deepin.dtk.style 1.0 as DStyle | 22 |
| import org.deepin.dtk.private 1.0 | 10 |
| import org.deepin.dtk as D | 8 |
| import org.deepin.dtk 1.0 as DTK | 6 |
| import org.deepin.dtk | 6 |
| import org.deepin.dtk.style as DS | 4 |
| import org.deepin.dtk.private 1.0 as DP | 4 |

### 3.2 QML DTK 组件使用（D.* 形式，全部）

| 排名 | 组件 | 使用次数 |
|------|------|---------|
| 1 | D.DTK | 453 |
| 2 | D.Palette | 286 |
| 3 | D.ColorSelector | 156 |
| 4 | D.DciIcon | 75 |
| 5 | D.SliderTipItem | 68 |
| 6 | D.Switch | 64 |
| 7 | D.ApplicationHelper | 58 |
| 8 | D.Label | 49 |
| 9 | D.DWindow | 49 |
| 10 | D.ComboBox | 48 |
| 11 | D.IconLabel | 43 |
| 12 | D.LineEdit | 39 |
| 13 | D.Color | 37 |
| 14 | D.DialogWindow | 32 |
| 15 | D.ItemDelegate | 26 |
| 16 | D.Button | 23 |
| 17 | D.RoundRectangle | 21 |
| 18 | D.ToolButton | 20 |
| 19 | D.TipsSlider | 20 |
| 20 | D.RecommandButton | 19 |
| 21 | D.MenuItem | 19 |
| 22 | D.ActionButton | 17 |
| 23 | D.BoxShadow | 13 |
| 24 | D.IconButton | 11 |
| 25 | D.StyledBehindWindowBlur | 10 |
| 26 | D.SpinBox | 10 |
| 27 | D.PasswordEdit | 7 |
| 28 | D.CheckBox | 7 |
| 29 | D.WindowManagerHelper | 6 |
| 30 | D.ProgressBar | 6 |
| 31 | D.ItemViewport | 6 |
| 32 | D.BoxInsetShadow | 6 |
| 33 | D.Menu | 5 |
| 34 | D.ListView | 5 |
| 35 | D.InsideBoxBorder | 5 |
| 36 | D.FocusBoxBorder | 5 |
| 37 | D.WarningButton | 4 |
| 38 | D.ToolTip | 4 |
| 39 | D.SortFilterModel | 4 |
| 40 | D.PlatformHandle | 4 |
| 41 | D.Slider | 3 |
| 42 | D.SearchEdit | 3 |
| 43 | D.InWindowBlur | 3 |
| 44 | D.DialogTitleBar | 3 |
| 45 | D.BoxPanel | 3 |
| 46 | D.TextField | 2 |
| 47 | D.SysInfo | 2 |
| 48 | D.OutsideBoxBorder | 2 |
| 49 | D.MenuSeparator | 2 |
| 50 | D.HighlightPanel | 2 |
| 51 | D.EditPanel | 2 |
| 52 | D.Control | 2 |
| 53 | D.BusyIndicator | 2 |
| 54 | D.TitleBar | 1 |
| 55 | D.ThemeMenu | 1 |
| 56 | D.ScrollBar | 1 |
| 57 | D.QuitAction | 1 |
| 58 | D.InWindowBlurImpl | 1 |
| 59 | D.HelpAction | 1 |
| 60 | D.FloatingPanel | 1 |
| 61 | D.Config | 1 |
| 62 | D.CheckDelegate | 1 |
| 63 | D.BackdropBlitter | 1 |
| 64 | D.ApplicationWindow | 1 |
| 65 | D.AboutDialog | 1 |
| 66 | D.AboutAction | 1 |

### 3.3 QML DTK 属性/方法详细统计

#### D.DTK 属性/方法（453次）

| 属性/方法 | 使用次数 | 说明 |
|----------|---------|------|
| fontManager | 238 | 字体管理器 |
| themeType | 74 | 主题类型 |
| makeIconPalette | 52 | 创建图标调色板 |
| makeColor | 37 | 创建颜色 |
| platformTheme | 19 | 平台主题 |
| palette | 14 | 调色板 |
| toColorType | 4 | 转换颜色类型 |
| makeIcon | 3 | 创建图标 |
| PressedState | 2 | 按下状态 |
| HoveredState | 2 | 悬停状态 |
| AboveOrder | 2 | 上层顺序 |
| NormalState | 1 | 正常状态 |
| isSoftwareRender | 1 | 是否软件渲染 |

#### D.ColorSelector 属性（156次）

| 属性 | 使用次数 |
|------|---------|
| textColor | 21 |
| backgroundColor | 18 |
| controlTheme | 16 |
| pressedColor | 14 |
| hoveredColor | 14 |
| controlState | 13 |
| dropShadowColor | 10 |
| innerShadowColor | 6 |
| checkedBackgroundColor | 6 |
| borderColor | 5 |
| insideBorderColor | 4 |
| hovered | 4 |
| contentColor | 4 |
| bgColor | 4 |
| pressed | 3 |
| family | 3 |
| scaleColor | 2 |
| outsideBorderColor | 2 |
| lineColor | 2 |
| shadowColor | 1 |
| separatorColor | 1 |
| placeholderTextColor | 1 |
| overlay | 1 |
| backgroundNoBlurColor | 1 |

#### D.DWindow 属性（49次）

| 属性 | 使用次数 |
|------|---------|
| enabled | 8 |
| windowRadius | 6 |
| themeType | 6 |
| enableBlurWindow | 6 |
| shadowColor | 5 |
| borderColor | 4 |
| shadowOffset | 3 |
| enableSystemMove | 3 |
| windowEffect | 2 |
| enableSystemResize | 2 |
| borderWidth | 2 |
| shadowRadius | 1 |

#### D.ApplicationHelper 属性（58次）

| 属性 | 使用次数 |
|------|---------|
| LightType | 39 |
| DarkType | 15 |
| handleHelpAction | 3 |
| setPaletteType | 1 |

---

## 四、结论

1. **主题适配是最核心需求**: DGuiApplicationHelper 总使用 580+ 次，instance() 调用 580 次
2. **字体管理需求突出**: DFontSizeManager 使用 522 次，T 枚举 462 次
3. **QML 开发是主流**: D.DTK 使用 453 次，D.Palette 286 次
4. **配置管理是基础设施**: DConfig 使用 178 次，create() 146 次
5. **调色板体系复杂**: DPalette 有 20+ 颜色角色，Text 138 次最高
6. **系统信息判断广泛**: DSysInfo 使用 93 次，用于 UOS 版本/类型判断
7. **日志管理统一**: DLogManager 三种 appender 共 110 次注册
8. **图标管理双轨**: DDciIcon(17) + DIconTheme(15) + DIcon(10) 共 42 次