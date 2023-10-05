# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Linker.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(677, 479)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(Qt.CustomContextMenu)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"../Static/link.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"color: #fff\n"
"}\n"
"QPushButton:hover { \n"
"background-color: rgb(47, 47, 47); \n"
"}\n"
"QListView::item {\n"
"border: none;\n"
"   border: 1px solid rgb(189, 189, 189);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}\n"
"QListView::item:hover {\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"QListView::item:selected {\n"
"   background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QMenu{\n"
"background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"#statusbar{\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#SB{\n"
"border: none;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"#button_add_file{\n"
"	border: 1px solid rgb(97, 131, 255);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}\n"
"#button_add_app{\n"
"	border: 1px solid rgb(52, 218, 2);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}\n"
"\n"
"#button_add_folder{\n"
"	border: 1px solid rgb(216, 0, 4);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}\n"
"\n"
"#lis"
                        "tView_folders{\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(216, 0, 4);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}\n"
"#listView_files{\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(97, 131, 255);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}\n"
"#listView_apps{\n"
"background-color: rgb(49, 49, 49);\n"
"border: 1px solid rgb(52, 218, 2);\n"
"	border-radius: 5px;\n"
"	padding:8px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_apps = QFrame(self.widget)
        self.frame_apps.setObjectName(u"frame_apps")
        self.frame_apps.setFrameShape(QFrame.StyledPanel)
        self.frame_apps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_apps)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_apps_list = QLabel(self.frame_apps)
        self.label_apps_list.setObjectName(u"label_apps_list")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_apps_list.setFont(font)

        self.verticalLayout_2.addWidget(self.label_apps_list, 0, Qt.AlignHCenter)

        self.line_5 = QFrame(self.frame_apps)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.listView_apps = QListView(self.frame_apps)
        self.listView_apps.setObjectName(u"listView_apps")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.listView_apps.setFont(font1)
        self.listView_apps.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView_apps.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView_apps.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.listView_apps)

        self.frame_iconApps = QFrame(self.frame_apps)
        self.frame_iconApps.setObjectName(u"frame_iconApps")
        self.frame_iconApps.setMinimumSize(QSize(0, 32))
        self.frame_iconApps.setFrameShape(QFrame.StyledPanel)
        self.frame_iconApps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_iconApps)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_iconApps = QLabel(self.frame_iconApps)
        self.label_iconApps.setObjectName(u"label_iconApps")
        self.label_iconApps.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.label_iconApps)

        self.label_pathApps = QLabel(self.frame_iconApps)
        self.label_pathApps.setObjectName(u"label_pathApps")

        self.horizontalLayout_4.addWidget(self.label_pathApps)


        self.verticalLayout_2.addWidget(self.frame_iconApps)

        self.button_add_app = QPushButton(self.frame_apps)
        self.button_add_app.setObjectName(u"button_add_app")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.button_add_app.setFont(font2)

        self.verticalLayout_2.addWidget(self.button_add_app)


        self.horizontalLayout_2.addWidget(self.frame_apps)

        self.frame_files = QFrame(self.widget)
        self.frame_files.setObjectName(u"frame_files")
        self.frame_files.setFrameShape(QFrame.StyledPanel)
        self.frame_files.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_files)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_files_list = QLabel(self.frame_files)
        self.label_files_list.setObjectName(u"label_files_list")
        self.label_files_list.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_files_list, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.frame_files)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.listView_files = QListView(self.frame_files)
        self.listView_files.setObjectName(u"listView_files")
        self.listView_files.setFont(font1)
        self.listView_files.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.listView_files)

        self.frame_iconFiles = QFrame(self.frame_files)
        self.frame_iconFiles.setObjectName(u"frame_iconFiles")
        self.frame_iconFiles.setMinimumSize(QSize(0, 32))
        self.frame_iconFiles.setFrameShape(QFrame.StyledPanel)
        self.frame_iconFiles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_iconFiles)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_iconFiles = QLabel(self.frame_iconFiles)
        self.label_iconFiles.setObjectName(u"label_iconFiles")
        self.label_iconFiles.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.label_iconFiles)

        self.label_pathFiles = QLabel(self.frame_iconFiles)
        self.label_pathFiles.setObjectName(u"label_pathFiles")

        self.horizontalLayout_5.addWidget(self.label_pathFiles)


        self.verticalLayout_3.addWidget(self.frame_iconFiles)

        self.button_add_file = QPushButton(self.frame_files)
        self.button_add_file.setObjectName(u"button_add_file")
        self.button_add_file.setFont(font2)
        self.button_add_file.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.button_add_file)


        self.horizontalLayout_2.addWidget(self.frame_files)

        self.frame_folders = QFrame(self.widget)
        self.frame_folders.setObjectName(u"frame_folders")
        self.frame_folders.setFrameShape(QFrame.StyledPanel)
        self.frame_folders.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_folders)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_folders_list = QLabel(self.frame_folders)
        self.label_folders_list.setObjectName(u"label_folders_list")
        self.label_folders_list.setFont(font2)
        self.label_folders_list.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.label_folders_list, 0, Qt.AlignHCenter)

        self.line = QFrame(self.frame_folders)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.listView_folders = QListView(self.frame_folders)
        self.listView_folders.setObjectName(u"listView_folders")
        self.listView_folders.setFont(font1)
        self.listView_folders.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView_folders.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.listView_folders)

        self.frame_iconFolders = QFrame(self.frame_folders)
        self.frame_iconFolders.setObjectName(u"frame_iconFolders")
        self.frame_iconFolders.setMinimumSize(QSize(0, 32))
        self.frame_iconFolders.setFrameShape(QFrame.StyledPanel)
        self.frame_iconFolders.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_iconFolders)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_iconFolders = QLabel(self.frame_iconFolders)
        self.label_iconFolders.setObjectName(u"label_iconFolders")
        self.label_iconFolders.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.label_iconFolders)

        self.label_pathFolders = QLabel(self.frame_iconFolders)
        self.label_pathFolders.setObjectName(u"label_pathFolders")

        self.horizontalLayout_6.addWidget(self.label_pathFolders)


        self.verticalLayout_4.addWidget(self.frame_iconFolders)

        self.button_add_folder = QPushButton(self.frame_folders)
        self.button_add_folder.setObjectName(u"button_add_folder")
        self.button_add_folder.setFont(font2)

        self.verticalLayout_4.addWidget(self.button_add_folder)


        self.horizontalLayout_2.addWidget(self.frame_folders)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listView_folders.clicked.connect(self.listView_files.clearSelection)
        self.listView_files.clicked.connect(self.listView_apps.clearSelection)
        self.listView_files.activated.connect(self.listView_apps.clearSelection)
        self.listView_apps.clicked.connect(self.listView_files.clearSelection)
        self.listView_folders.clicked.connect(self.listView_apps.clearSelection)
        self.listView_files.clicked.connect(self.listView_folders.clearSelection)
        self.listView_apps.clicked.connect(self.listView_folders.clearSelection)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Linker", None))
        self.label_apps_list.setText(QCoreApplication.translate("MainWindow", u"Applications List", None))
        self.label_iconApps.setText("")
        self.label_pathApps.setText("")
        self.button_add_app.setText(QCoreApplication.translate("MainWindow", u"Add App +", None))
        self.label_files_list.setText(QCoreApplication.translate("MainWindow", u"Files List", None))
        self.label_iconFiles.setText("")
        self.label_pathFiles.setText("")
        self.button_add_file.setText(QCoreApplication.translate("MainWindow", u"Add File +", None))
        self.label_folders_list.setText(QCoreApplication.translate("MainWindow", u"Folders List", None))
        self.label_iconFolders.setText("")
        self.label_pathFolders.setText("")
        self.button_add_folder.setText(QCoreApplication.translate("MainWindow", u"Add Folder +", None))
    # retranslateUi

