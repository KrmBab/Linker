# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_rename.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout,
                               QLineEdit, QPushButton, QVBoxLayout,
                               QWidget)


class Ui_Dialog_rename(object):
    def setupUi(self, Dialog_rename):
        if not Dialog_rename.objectName():
            Dialog_rename.setObjectName(u"Dialog_rename")
        Dialog_rename.resize(219, 100)
        Dialog_rename.setMinimumSize(QSize(219, 0))
        Dialog_rename.setMaximumSize(QSize(16777215, 100))
        Dialog_rename.setStyleSheet(u"*{\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "color: #fff\n"
                                    "}\n"
                                    "QPushButton:hover { \n"
                                    "background-color: rgb(47, 47, 47); \n"
                                    "}\n"
                                    "QLineEdit {\n"
                                    "border: none;\n"
                                    "   border: 1px solid rgb(189, 189, 189);\n"
                                    "	border-radius: 5px;\n"
                                    "	padding:8px;\n"
                                    "}\n"
                                    "\n"
                                    "#button_save{\n"
                                    "	border: 1px solid rgb(14, 172, 51);\n"
                                    "	border-radius: 5px;\n"
                                    "	padding:8px;\n"
                                    "}\n"
                                    "#button_cancel{\n"
                                    "	border: 1px solid rgb(213, 50, 22);\n"
                                    "	border-radius: 5px;\n"
                                    "	padding:8px;\n"
                                    "}\n"
                                    "")
        self.verticalLayout = QVBoxLayout(Dialog_rename)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog_rename)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_save = QPushButton(self.frame)
        self.button_save.setObjectName(u"button_save")

        self.horizontalLayout.addWidget(self.button_save)

        self.button_cancel = QPushButton(self.frame)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.lineEdit.raise_()
        self.frame.raise_()

        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog_rename)

        QMetaObject.connectSlotsByName(Dialog_rename)

    # setupUi

    def retranslateUi(self, Dialog_rename):
        Dialog_rename.setWindowTitle(QCoreApplication.translate("Dialog_rename", u"Rename", None))
        self.button_save.setText(QCoreApplication.translate("Dialog_rename", u"save", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog_rename", u"cancel", None))
    # retranslateUi
