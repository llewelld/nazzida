# SPDX-FileCopyrightText: (C) 2022 Matthias Fehring / www.huessenbergnetz.de
# SPDX-License-Identifier: GPL-3.0-or-later

cmake_minimum_required(VERSION 3.16.0)
cmake_policy(SET CMP0048 NEW)

project(nazzida
    VERSION 1.0.1
    DESCRIPTION "Personal Fluid Balance Protocol"
    HOMEPAGE_URL "https://github.com/Huessenbergnetz/nazzida"
    LANGUAGES CXX)

include(FindPkgConfig)
include(GNUInstallDirs)

set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(TARGETSYSTEM "sfos" CACHE STRING "Target system to build the application for, currently supported: sfos, kirigami")

if (${TARGETSYSTEM} STREQUAL "sfos")
    message(STATUS "Building Nazzida for SailfishOS")

    find_package (Qt5 COMPONENTS Core Qml Gui Quick Sql LinguistTools REQUIRED)

    set(NAZZIDA_EXE_OUTPUT_NAME harbour-nazzida)
    set(HBNSC_APPNAME ${NAZZIDA_EXE_OUTPUT_NAME} CACHE STRING "Name of the application the HBN SFOS Components are used for. Used for installation values.")
    set(CMAKE_INSTALL_LIBDIR ${CMAKE_INSTALL_DATADIR}/${NAZZIDA_EXE_OUTPUT_NAME}/lib)
    set(HBNSC_WITH_OPENSSL OFF)
    set(HBNSC_WITH_FIRFUORIDA On)
    set(HBNSC_LICENSES "GPLv3;LGPLv2_1;BSD-3;CC-BY-4_0")
    set(NAZZIDA_I18NDIR ${CMAKE_INSTALL_DATADIR}/${NAZZIDA_EXE_OUTPUT_NAME}/translations)
    set(NAZZIDA_QMLDIR ${CMAKE_INSTALL_DATADIR}/${NAZZIDA_EXE_OUTPUT_NAME}/qml)

    list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/3rdparty/HBN_SFOS_Cmake)

    add_subdirectory(3rdparty)
    add_subdirectory(SailfishOS)

    add_custom_target(specfiles
        SOURCES
            rpm/harbour-nazzida.changes
            rpm/harbour-nazzida.spec
            rpm/harbour-nazzida.yaml
    )
endif (${TARGETSYSTEM} STREQUAL "sfos")

if (${TARGETSYSTEM} STREQUAL "kirigami")
    message(STATUS "Building Nazzida for Kirigami")

    set(KF_MIN_VERSION "5.76.0")
    set(QT_MIN_VERSION "5.12.0")

    find_package(ECM ${KF_MIN_VERSION} REQUIRED NO_MODULE)

    list(APPEND CMAKE_MODULE_PATH ${ECM_MODULE_PATH})

    include(KDEInstallDirs)
    include(KDECMakeSettings)
    include(KDECompilerSettings NO_POLICY_SCOPE)

    find_package(Qt5 ${QT_MIN_VERSION} REQUIRED NO_MODULE COMPONENTS Core Quick Test Gui QuickControls2 Widgets Sql)
    find_package(KF5 ${KF_MIN_VERSION} REQUIRED COMPONENTS Kirigami2 I18n CoreAddons)
    find_package(FirfuoridaQt5 REQUIRED)

    set(NAZZIDA_I18NDIR "${CMAKE_INSTALL_DATADIR}/nazzida/translations" CACHE PATH "Installation destination for translation files.")

    add_subdirectory(Kirigami)

    feature_summary(WHAT ALL INCLUDE_QUIET_PACKAGES FATAL_ON_MISSING_REQUIRED_PACKAGES)
endif (${TARGETSYSTEM} STREQUAL "kirigami")
