cmake_minimum_required(VERSION 3.16)

project(weather-tray-plugin LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets)
find_package(Dtk6 REQUIRED COMPONENTS Widget Gui)

add_library(weather SHARED
    weatherplugin.h
    weatherplugin.cpp
    weatherwidget.h
    weatherwidget.cpp
    weatherdata.h
    weatherdata.cpp
    weatherapplet.h
    weatherapplet.cpp
    weather.json
    weather.qrc
)

target_compile_definitions(weather PRIVATE QT_PLUGIN)

target_include_directories(weather PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Include dde-tray-loader interface headers
# Adjust this path to your dde-tray-loader source directory or install prefix
if(DEFINED TRAY_LOADER_INTERFACE_DIR)
    target_include_directories(weather PRIVATE ${TRAY_LOADER_INTERFACE_DIR})
else()
    find_package(dde-tray-loader-dev REQUIRED)
endif()

target_link_libraries(weather PRIVATE
    Dtk6::Widget
    Dtk6::Gui
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
)

install(TARGETS weather LIBRARY DESTINATION lib/dde-dock/plugins)
