import ctypes
import os
import sys

from PySide6.QtCore import QStringListModel, Qt, QSize
from PySide6.QtGui import QDropEvent, QDragEnterEvent, QIcon
from PySide6.QtWidgets import QMainWindow

from Widgets.Linker import Ui_MainWindow
from .CutomWidget import ContextMenu, StatusBar
from .Manager import DBManager


def check_single_instance():
    # Define the path to the lock file
    mutex_name = "LinkerMutex"
    # Attempt to create a named mutex
    mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)

    # Check if the mutex already exists (another instance is running)
    if ctypes.windll.kernel32.GetLastError() == 183:
        print("Another instance of the application is already running.")
        sys.exit(1)

class Widget(DBManager, QMainWindow):
    __foldersCount = 0
    __filesCount = 0
    __appsCount = 0
    models_list = None
    def __init__(self, parent=None):
        super().__init__(self.models_list, self.__selectedItems)
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        icon = QIcon()
        icon.addFile("_internal/Static/link.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.setupUi(self)
        self.setWindowIcon(icon)
        self.dialog_rename.setWindowIcon(icon)

        self.ui.button_add_folder.clicked.connect(self.add_folder)
        self.ui.button_add_file.clicked.connect(self.add_file)
        self.ui.button_add_app.clicked.connect(self.add_app)

        self.model_folders = QStringListModel()
        self.model_folders.setObjectName("folders")

        self.model_apps = QStringListModel()
        self.model_apps.setObjectName("apps")

        self.model_files = QStringListModel()
        self.model_files.setObjectName("files")

        self.models_list = {self.model_folders.objectName():self.model_folders,
                            self.model_apps.objectName():self.model_apps,
                            self.model_files.objectName(): self.model_files,}

        self.update_from_db()

        self.ui.listView_folders.setModel(self.model_folders)
        self.ui.listView_apps.setModel(self.model_apps)
        self.ui.listView_files.setModel(self.model_files)

        self.ui.listView_folders.doubleClicked.connect(self.open_item)
        self.ui.listView_files.doubleClicked.connect(self.open_item)
        self.ui.listView_apps.doubleClicked.connect(self.open_item)

        self.ui.listView_folders.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.listView_files.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.listView_apps.customContextMenuRequested.connect(self.show_context_menu)

        self.ui.listView_folders.clicked.connect(self.show_path)
        self.ui.listView_apps.clicked.connect(self.show_path)
        self.ui.listView_files.clicked.connect(self.show_path)

        #########################
        # Create a context menu
        context_menu_actions = {"Open": self.open_item,
                                "Open_path": self.open_item_dir,
                                "Copy_path": self.copy_item_path,
                                "Rename": self.rename_item,
                                "Delete": self.delete_item}

        self.context_menu = ContextMenu(context_menu_actions)
        self.statusbar = StatusBar(self.ui.statusbar)

        self.update_status()



    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            model = None
            file_path = mime_data.urls()[0].toLocalFile()
            file_name = os.path.basename(file_path)
            if os.path.isdir(file_path):
                model = self.model_folders
            elif ".exe" not in file_name:
                model = self.model_files
            else:
                model = self.model_apps

            msg = self.DB.add_item(model.objectName(), file_name, file_path)
            self.update_from_db(msg)
            if msg is None:
                self.messageBox.set_info(f"item added to {model.objectName()} list")
                self.messageBox.exec()

    def __selectedItems(self) -> (None, QStringListModel):
        items_files = self.ui.listView_files.selectedIndexes()
        items_folder = self.ui.listView_folders.selectedIndexes()
        items_apps = self.ui.listView_apps.selectedIndexes()

        if items_files:       return items_files,  self.model_files, self.ui.label_iconFiles, self.ui.label_pathFiles
        elif items_folder:    return items_folder, self.model_folders, self.ui.label_iconFolders, self.ui.label_pathFolders
        elif items_apps:      return items_apps,   self.model_apps, self.ui.label_iconApps, self.ui.label_pathApps
        else:                 return None, None, None, None


    def keyPressEvent(self, event):
        # This function is called when a key is pressed
        key = event.key()
        if key == Qt.Key.Key_Delete:
            self.delete_item()
        if key == 16777220:
            self.open_item()

    def show_context_menu(self, position):
        listeviws = [self.ui.listView_folders, self.ui.listView_files, self.ui.listView_apps]
        for lv in listeviws:
            if lv != self.sender():
                lv.clearSelection()

        self.show_path()
        self.context_menu.show_context_menu(position, self.sender())

