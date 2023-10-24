import ctypes
import os
import sys
import winreg
from time import sleep

import win32com.client
from PySide6.QtCore import QStringListModel, Qt, QSize
from PySide6.QtGui import QDropEvent, QDragEnterEvent, QIcon
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QApplication

from Widgets.Linker import Ui_MainWindow
from .CutomWidget import ContextMenu, StatusBar, MessageBox
from .DataBase import DataBase
from .Manager import Manager, DataCenter

icon_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\Static\\link.ico"
local_socket_name = "Linker"

def check_single_instance():
    # Define the path to the lock file
    mutex_name = "LinkerMutex"
    # Attempt to create a named mutex
    mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)

    # Check if the mutex already exists (another instance is running)
    if ctypes.windll.kernel32.GetLastError() == 183:
        # Connect to the local server of the existing instance
        local_socket = QLocalSocket()
        local_socket.connectToServer(local_socket_name)

        if local_socket.waitForConnected(1000):
            local_socket.write(b"activate")
            local_socket.waitForBytesWritten()
            local_socket.disconnectFromServer()
        sys.exit(0)

class Widget(Manager, QMainWindow):
    ###
    db_path = os.path.join(os.getenv('APPDATA'), 'Linker/LinkerDB.db')
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs',
                                  'Startup') + "\\Linker.lnk"
    ###

    __foldersCount = 0
    __filesCount = 0
    __appsCount = 0

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        icon = QIcon()
        icon.addFile(icon_path, QSize(), QIcon.Normal, QIcon.Off)

        self.ui.setupUi(self)
        self.setWindowIcon(icon)

        self.model_folders = QStringListModel()
        self.model_folders.setObjectName("folders")

        self.model_apps = QStringListModel()
        self.model_apps.setObjectName("apps")

        self.model_files = QStringListModel()
        self.model_files.setObjectName("files")

        models_list = {self.model_folders.objectName(): {"model": self.model_folders, "class": self.ui.class_folders},
                       self.model_apps.objectName(): {"model": self.model_apps, "class": self.ui.class_apps},
                       self.model_files.objectName(): {"model": self.model_files, "class": self.ui.class_files}}

        listsViews = [
            {"list": self.ui.listView_apps, "icon": self.ui.label_iconApps, "path": self.ui.label_pathApps},
            {"list": self.ui.listView_folders, "icon": self.ui.label_iconFolders, "path": self.ui.label_pathFolders},
            {"list": self.ui.listView_files, "icon": self.ui.label_iconFiles, "path": self.ui.label_pathFiles}
        ]

        dataBase = DataBase(self.db_path)
        statusbar = StatusBar(self.ui.statusbar)

        self.dataCenter = DataCenter(
            models_dict=models_list,
            listsViews_dict=listsViews,
            dataBase=dataBase,
            iconLinker=icon,
            statusbar=statusbar)

        super().__init__(self.dataCenter)

        self.ui.button_add_folder.clicked.connect(self.add_folder)
        self.ui.button_add_file.clicked.connect(self.add_file)
        self.ui.button_add_app.clicked.connect(self.add_app)

        self.ui.listView_folders.setModel(self.model_folders)
        self.ui.listView_apps.setModel(self.model_apps)
        self.ui.listView_files.setModel(self.model_files)

        # connect to functions
        for lst in listsViews:
            lst["list"].doubleClicked.connect(self.open_item)
            lst["list"].customContextMenuRequested.connect(
                lambda pos, obj=lst["list"]: self.show_contextMenu_items(pos, obj))
            lst["list"].clicked.connect(self.show_path_and_icon)

        ########
        self.update_category_fromDB()
        ########

        # connect to functions
        self.ui.class_apps.currentTextChanged.connect(self.update_apps_fromDB)
        self.ui.class_files.currentTextChanged.connect(self.update_files_fromDB)
        self.ui.class_folders.currentTextChanged.connect(self.update_folders_fromDB)

        self.update_from_db()
        #########################
        # Create a context menu
        context_menu_actions = [["+Add_to_category+", self.Add_to_category, False],
                                ["Open", self.open_item, False],
                                ["Open_path", self.open_item_dir, False],
                                ["Copy_path", self.copy_item_path, False],
                                ["Rename", self.rename_item, False],
                                ["Delete", self.delete_item, False]]

        contextMenu_category_actions = [["Edite", self.show_category_menu, False]]

        self.context_menu = ContextMenu(context_menu_actions)
        self.contextMenu_category = ContextMenu(contextMenu_category_actions)

        categoryList = [self.ui.class_apps, self.ui.class_folders, self.ui.class_files]
        for cat in categoryList:
            cat.customContextMenuRequested.connect(
                lambda pos, obj=cat: self.contextMenu_category.show_contextMenu(pos, obj))

        self.update_status()

        tray_menu = ContextMenu([["autorun", self.autorun, True],
                                 ["Open", lambda reason=True: self.show_main_window(reason), False],
                                 ["Exit", self.close, False]])

        tray_menu.set_check_stat("autorun",os.path.exists(self.startup_folder))

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)  # Icône de l'ordinateur
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.show_main_window)
        self.tray_icon.show()

        # Create a local server for communication with other instances
        self.local_server = QLocalServer()
        self.local_server.listen(local_socket_name)
        self.local_server.event = self.server

    def server(self, event):
        '''
        this function show the running instance if user tray to run another instance
        :param event:
        :return:
        '''
        self.show()
        self.showNormal()
        self.activateWindow()
        print(event)

    # region Tray
    def show_main_window(self, reason):
        '''
        this function shows the MainWindow on tray icon doubleclick
        :param reason: tray icon activated signal
        :return:
        '''
        if reason == QSystemTrayIcon.DoubleClick or reason is True:
            self.show()
            self.showNormal()
            self.activateWindow()

    def closeEvent(self, event):
        '''
        change the close event to hide the window
        :param event: closeEvent
        :return:
        '''
        if event.spontaneous():
            event.ignore()
            self.showMinimized()
            sleep(0.2)
            self.hide()

        else:
            QApplication.quit()

    # endregion

    def Add_to_category(self):
        '''
        this function shows the add to category Dialog
        :return:
        '''
        self.category_dialog.show_window(self.context_menu.contextmenuObject)

    def show_category_menu(self) -> None:
        '''
        this function shows the category menu
        :return:
        '''
        self.category_menu.show_category_menu(self.contextMenu_category.contextmenuObject)

    def dragEnterEvent(self, event: QDragEnterEvent):
        '''
        Accepts the drag item if it has URLs path.

        :param event: QDragEnterEvent object.
        :return: None
        '''
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        '''
        this function checks the dropped item to determinate in witch DB table it should be added
        :param event: QDropEvent
        :return:
        '''
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            for file in mime_data.urls():
                file_path = file.toLocalFile()
                if ".lnk" in file_path:
                    shell = win32com.client.Dispatch("WScript.Shell")
                    file_path = shell.CreateShortCut(file_path).Targetpath
                file_name = os.path.basename(file_path)
                if os.path.isdir(file_path):
                    model = self.model_folders
                elif ".exe" not in file_name:
                    model = self.model_files
                else:
                    model = self.model_apps

                msg = self.dataCenter.dataBase.add_item(model.objectName(), file_name, file_path)
                self.update_from_db(msg)
                self.update_status()
                if msg is None:
                    self.messageBox.set_info(f"item added to {model.objectName()} list")

    def keyPressEvent(self, event):
        '''
        this function add action to keyboard keys (Enter:open item, Delete: delete item)
        :param event:
        :return:
        '''
        # This function is called when a key is pressed
        key = event.key()
        if key == Qt.Key.Key_Delete:
            self.delete_item()
        if key == 16777220:
            self.open_item()

    def show_contextMenu_items(self, position, obj):
        '''
        this function shows listview item contextmenu
        :param position: right clic mouse position
        :param obj: current listview
        :return:
        '''
        self.show_path_and_icon()
        self.context_menu.show_contextMenu_position(position, obj)

    def autorun(self, create=False):
        '''
        Update the autorun settings.
        :param create: boolean indicating whether to create or remove the autorun shortcut
        '''
        if create:
            # Get the absolute path of the script
            script_path = os.path.abspath(sys.argv[0])
            # Create a Windows Script Shell object
            shell = win32com.client.Dispatch("WScript.Shell")
            # Create a shortcut object in the startup folder
            shortcut = shell.CreateShortcut(self.startup_folder)
            # Set the target path of the shortcut to the script path
            shortcut.TargetPath = script_path
            # Save the shortcut
            shortcut.Save()
        else:
            # Remove the autorun shortcut
            os.remove(self.startup_folder)
