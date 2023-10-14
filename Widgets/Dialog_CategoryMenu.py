# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_CategoryMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout,
                               QListView, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

class Ui_Dialog_CategoryMenu(object):
    def setupUi(self, Dialog_CategoryMenu):
        if not Dialog_CategoryMenu.objectName():
            Dialog_CategoryMenu.setObjectName(u"Dialog_CategoryMenu")
        Dialog_CategoryMenu.resize(292, 307)
        Dialog_CategoryMenu.setStyleSheet(u"*{\n"
"	background-color: rgb(74, 74, 74);\n"
"	color: #fff\n"
"}\n"
"\n"
" QPushButton{\n"
"	border: 1px solid rgb(182, 182, 182);\n"
"    border-radius: 5px;\n"
"    padding:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QListView{\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px;\n"
"padding:8px;\n"
"}\n"
"\n"
"QListView:item{\n"
"border: none;\n"
"border-bottom: 1px solid rgb(189, 189, 189);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Dialog_CategoryMenu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog_CategoryMenu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listView_category = QListView(self.widget)
        self.listView_category.setObjectName(u"listView_category")
        font = QFont()
        font.setPointSize(12)
        self.listView_category.setFont(font)

        self.horizontalLayout_2.addWidget(self.listView_category)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_add = QPushButton(self.frame_2)
        self.button_add.setObjectName(u"button_add")

        self.verticalLayout.addWidget(self.button_add)

        self.button_edit = QPushButton(self.frame_2)
        self.button_edit.setObjectName(u"button_edit")

        self.verticalLayout.addWidget(self.button_edit)

        self.button_delete = QPushButton(self.frame_2)
        self.button_delete.setObjectName(u"button_delete")

        self.verticalLayout.addWidget(self.button_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog_CategoryMenu)

        QMetaObject.connectSlotsByName(Dialog_CategoryMenu)
    # setupUi

    def retranslateUi(self, Dialog_CategoryMenu):
        Dialog_CategoryMenu.setWindowTitle(QCoreApplication.translate("Dialog_CategoryMenu", u"Dialog", None))
        self.button_add.setText(QCoreApplication.translate("Dialog_CategoryMenu", u"Add +", None))
        self.button_edit.setText(QCoreApplication.translate("Dialog_CategoryMenu", u"Edit", None))
        self.button_delete.setText(QCoreApplication.translate("Dialog_CategoryMenu", u"Delete", None))
    # retranslateUi

