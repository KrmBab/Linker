import os
from typing import Dict, Any, List

from PySide6.QtCore import QStringListModel, QUrl, QFileInfo
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QFileDialog, QFileIconProvider, QApplication, QListView, QLabel, QComboBox

from Widgets.Dialog_rename import Ui_Dialog_rename
from .DataBase import DataBase
from .CutomWidget import MessageBox, Rename, AddToClass


class DBManager():
    def __init__(self):

        self.models_list = None
        self.listsViews:[Dict[str:QListView, str:QLabel, str:QLabel]] = []
        self.comboBoxs:[Dict[str:QComboBox, str:QComboBox, str:QComboBox]] = []

        self.statusbar = None

        self.dialog_rename = Rename()
        self.dialog_addToClass = AddToClass()
        self.class_tabe = None
        self.dialog_addToClass.button_addClass.clicked.connect(self.add_class)
        self.dialog_addToClass.button_removeClass.clicked.connect(self.remove_class)

        self.messageBox = MessageBox()
        self.clipboard = QApplication.clipboard()
        self.DB = DataBase("data/LinkerDB.db")

    def remove_class(self):

        msg = self.DB.remove_class(self.class_tabe.objectName(), self.dialog_addToClass.get_class())
        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        else:
            self.dialog_addToClass.rest_items()
            class_items = self.DB.get_class(self.class_tabe.objectName())
            self.dialog_addToClass.update_items(class_items)
            # self.update_class_fromDB()
    def add_class(self):

        self.dialog_rename.lineEdit.setText("")
        save = self.dialog_rename.exec()
        if save:
            class_name = self.dialog_rename.lineEdit.text()
            msg = self.DB.add_class( self.class_tabe.objectName(),class_name)
            if msg is not None:
                self.messageBox.set_error(msg)
                self.messageBox.exec()
            else:
                self.dialog_addToClass.rest_items()
                class_items = self.DB.get_class(self.class_tabe.objectName())
                self.dialog_addToClass.update_items(class_items)
                # self.update_class_fromDB()
    def update_class_fromDB(self):
        for cls in self.models_list.values():
            cls["class"].clear()
            cls["class"].addItem("")
            cls["class"].addItems(self.DB.get_class(cls["class"].objectName()))
        pass

    def Get_selectedItems(self):
        for LV in self.listsViews:
            items = LV["list"].selectedIndexes()
            if items:
                return items, LV["list"].model(), LV["icon"], LV["path"]
        return None, None, None, None

    def get_exe_icon(self,exe_path):
        icon_provider = QFileIconProvider()
        file_info = QFileInfo(exe_path)
        icon = icon_provider.icon(file_info)
        icon = icon.pixmap(30, 30)
        return icon

    def update_status(self):
        filesCount = self.models_list["files"]["model"].rowCount()
        foldersCount = self.models_list["folders"]["model"].rowCount()
        appsCount = self.models_list["apps"]["model"].rowCount()

        self.statusbar.set_status(f"Apps : {appsCount} | Files : {filesCount} | Folders : "
                                      f"{foldersCount}")

    def show_path(self):
        items, model, label_icon, label_name = self.Get_selectedItems()
        if items:
            path = self.DB.get_item_path(model.objectName(), items[0].data())
            self.statusbar.set_message(f"{path}")

            label_icon.setPixmap(self.get_exe_icon(path))
            label_name.setText(os.path.basename(path))

    def update_from_db(self, msg:str=None):

        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        for model in self.models_list.values():
            model["model"].setStringList(self.DB.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def update_apps_fromDB(self):
        model = self.models_list["apps"]
        model["model"].setStringList(self.DB.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def update_folders_fromDB(self):
        model = self.models_list["folders"]
        model["model"].setStringList(self.DB.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def update_files_fromDB(self):
        model = self.models_list["files"]
        model["model"].setStringList(self.DB.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def add_folder(self):
        # Create a folder selection dialog
        selected_folder = QFileDialog.getExistingDirectory()
        if selected_folder != "":
            folder_name = os.path.basename(selected_folder)
            msg = self.DB.add_item(self.models_list["folders"]["model"].objectName(), folder_name, selected_folder)
            self.update_from_db(msg)

    def add_file(self):
        # Create a folder selection dialog
        selected_file = QFileDialog.getOpenFileName()
        if selected_file[0] != "":
            file_name = os.path.basename(selected_file[0])

            if ".exe" not in file_name:
                msg = self.DB.add_item(self.models_list["files"]["model"].objectName(), file_name, selected_file[0])

            else:
                # Show the warning message box and wait for user interaction
                self.messageBox.set_warning("This is an .exe file it will be add to Apps list")
                self.messageBox.exec()
                msg = self.DB.add_item(self.models_list["apps"]["model"].objectName(), file_name, selected_file[0])

            self.update_from_db(msg)

    def add_app(self):
        # Create a folder selection dialog
        selected_app = QFileDialog.getOpenFileName(filter="*.exe")
        if selected_app[0] != "":
            app_name = os.path.basename(selected_app[0])
            msg = self.DB.add_item(self.models_list["apps"]["model"].objectName(), app_name, selected_app[0])
            self.update_from_db(msg)

    def rename_item(self):
        items, model, _, _ = self.Get_selectedItems()
        old_name = items[0].data()
        self.dialog_rename.lineEdit.setText(old_name)
        save = self.dialog_rename.exec()
        if save:
            new_name = self.dialog_rename.lineEdit.text()
            if new_name != old_name:
                msg = self.DB.change_item_name(model.objectName(), old_name, new_name)
                self.update_from_db(msg)

    def delete_item(self):
        items, model, icon, name = self.Get_selectedItems()
        icon.setPixmap(QPixmap())
        name.setText("")
        self.statusbar.set_message("")
        if items:
            msg = None
            for itm in items:
                msg = self.DB.delete_item(model.objectName(), itm.data())
            self.update_from_db(msg)
            self.update_status()

    def open_item(self):
        items, model , _, _= self.Get_selectedItems()

        for itm in items:
            itm_path = self.DB.get_item_path(model.objectName(),itm.data())
            itm_url = QUrl.fromLocalFile(itm_path)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def open_item_dir(self):
        items, model, _, _ = self.Get_selectedItems()
        for itm in items:
            itm_path = self.DB.get_item_path(model.objectName(),itm.data())
            itm_dir = os.path.dirname(itm_path)
            itm_url = QUrl.fromLocalFile(itm_dir)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def copy_item_path(self):
        items, model, _, _ = self.Get_selectedItems()

        for itm in items:
            itm_path = self.DB.get_item_path(model.objectName(),itm.data())
            if os.path.exists(itm_path):
                self.clipboard.setText(itm_path)
            else:
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def add_toClass(self):
        items, model, _, _ = self.Get_selectedItems()

        for mdl in self.models_list.values():
            if mdl["model"] == model:
                self.class_tabe = mdl["class"]
                break

        class_items = self.DB.get_class(self.class_tabe.objectName())
        self.dialog_addToClass.update_items(class_items)
        add = self.dialog_addToClass.exec()
        className = self.dialog_addToClass.get_class()
        self.dialog_addToClass.rest_items()

        if add:
            self.DB.set_class(model.objectName(), items[0].data(), className)

        self.update_class_fromDB()