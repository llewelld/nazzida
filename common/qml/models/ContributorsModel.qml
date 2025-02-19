/*
 * SPDX-FileCopyrightText: (C) 2022 Matthias Fehring / www.huessenbergnetz.de
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

import QtQuick 2.2

ListModel {
    id: contModel
    ListElement {
        name: "Matthias Fehring (Buschmann)"
        role: ""
        section: ""
        website: "https://www.buschmann23.de/?pk_campaign=Sailfish-App-Nazzida&pk_kwd=ContributorsList"
        twitter: "buschmann23"
        github: "buschmann23"
    }

    Component.onCompleted: {
        //: contributor role
        //% "Main developer, Nazzida creator"
        contModel.get(0).role = qsTrId("nazzida-author-role")
        //: the section a contributor belongs to
        //% "Author"
        contModel.get(0).section = qsTrId("nazzida-author-section")
    }
}
