# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_addToClass.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog_addToClass(object):
    def setupUi(self, Dialog_addToClass):
        if not Dialog_addToClass.objectName():
            Dialog_addToClass.setObjectName(u"Dialog_addToClass")
        Dialog_addToClass.setWindowModality(Qt.ApplicationModal)
        Dialog_addToClass.resize(317, 105)
        Dialog_addToClass.setMinimumSize(QSize(219, 0))
        Dialog_addToClass.setMaximumSize(QSize(16777215, 150))
        icon = QIcon()
        icon.addFile(u"../_internal/Static/link.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_addToClass.setWindowIcon(icon)
        Dialog_addToClass.setStyleSheet(u"*{\n"
"                background-color: rgb(74, 74, 74);\n"
"                color: #fff\n"
"                }\n"
"                QPushButton:hover {\n"
"                background-color: rgb(47, 47, 47);\n"
"                }\n"
"\n"
"                QComboBox:hover {\n"
"                background-color: rgb(47, 47, 47);\n"
"                }\n"
"                QComboBox{\n"
"                border: 1px solid rgb(195, 195, 195);\n"
"                background-color: rgb(74, 74, 74);\n"
"                border-radius: 5px;\n"
"                padding:5px;\n"
"                }\n"
"                QComboBox QAbstractItemView {\n"
"                background-color: rgb(47, 47, 47);\n"
"                border: none;\n"
"                border: 1px solid rgb(189, 189, 189);\n"
"                border-radius: 5px;\n"
"                padding:5px;\n"
"                }\n"
"\n"
"                QComboBox::drop-down{\n"
"                background-color: rgb(47, 47, 47);\n"
"                border-radius: 5px;\n"
""
                        "                padding:5px;\n"
"                }\n"
"\n"
"                #button_addClass{\n"
"                border: 1px solid rgb(14, 172, 51);\n"
"                border-radius: 5px;\n"
"                padding:8px;\n"
"                }\n"
"                #button_removeClass{\n"
"                border: 1px solid rgb(213, 50, 22);\n"
"                border-radius: 5px;\n"
"                padding:9px;\n"
"                }\n"
"\n"
"                #button_save{\n"
"                border: 1px solid rgb(14, 172, 51);\n"
"                border-radius: 5px;\n"
"                padding:8px;\n"
"                }\n"
"                #button_cancel{\n"
"                border: 1px solid rgb(213, 50, 22);\n"
"                border-radius: 5px;\n"
"                padding:8px;\n"
"                }\n"
"            ")
        Dialog_addToClass.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog_addToClass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.class_items = QComboBox(Dialog_addToClass)
        self.class_items.setObjectName(u"class_items")
        self.class_items.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.class_items)

        self.widget = QWidget(Dialog_addToClass)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog_addToClass)

        QMetaObject.connectSlotsByName(Dialog_addToClass)
    # setupUi

    def retranslateUi(self, Dialog_addToClass):
        Dialog_addToClass.setWindowTitle(QCoreApplication.translate("Dialog_addToClass", u"Categorys", None))
        self.button_save.setText(QCoreApplication.translate("Dialog_addToClass", u"save", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog_addToClass", u"cancel", None))
    # retranslateUi

