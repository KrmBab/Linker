import os
from typing import Dict

from PySide6.QtCore import QStringListModel, QUrl, QFileInfo
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QFileDialog, QFileIconProvider, QApplication

from Classes.DataBase import DataBase
from .CutomWidget import MessageBox, Rename


class DBManager():
    def __init__(self, models_list:Dict[str, QStringListModel], MethodeSelectedItems):

        self.models_list = models_list
        self.MethodeSelectedItems = MethodeSelectedItems
        self.statusbar = None

        self.dialog_rename = Rename()
        self.messageBox = MessageBox()
        self.clipboard = QApplication.clipboard()
        self.DB = DataBase("data/LinkerDB.db")

    def get_exe_icon(self,exe_path):
        icon_provider = QFileIconProvider()
        file_info = QFileInfo(exe_path)
        icon = icon_provider.icon(file_info)
        icon = icon.pixmap(30, 30)
        return icon

    def update_status(self):
        filesCount = self.models_list["files"].rowCount()
        foldersCount = self.models_list["folders"].rowCount()
        appsCount = self.models_list["apps"].rowCount()

        self.statusbar.set_status(f"Apps : {appsCount} | Files : {filesCount} | Folders : "
                                      f"{foldersCount}")

    def show_path(self):
        items, model, label_icon, label_name = self.MethodeSelectedItems()
        path = self.DB.get_item_path(model.objectName(), items[0].data())
        self.statusbar.set_message(f"{path}")

        label_icon.setPixmap(self.get_exe_icon(path))
        label_name.setText(os.path.basename(path))

    def update_from_db(self, msg:str=None):

        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        for model in self.models_list.values():
            model.setStringList(self.DB.get_all_names(model.objectName()))

    def add_folder(self):
        # Create a folder selection dialog
        selected_folder = QFileDialog.getExistingDirectory()
        if selected_folder != "":
            folder_name = os.path.basename(selected_folder)
            msg = self.DB.add_item(self.models_list["folders"].objectName(), folder_name, selected_folder)
            self.update_from_db(msg)

    def add_file(self):
        # Create a folder selection dialog
        selected_file = QFileDialog.getOpenFileName()
        if selected_file[0] != "":
            file_name = os.path.basename(selected_file[0])

            if ".exe" not in file_name:
                msg = self.DB.add_item(self.models_list["files"].objectName(), file_name, selected_file[0])

            else:
                # Show the warning message box and wait for user interaction
                self.messageBox.set_warning("This is an .exe file it will be add to Apps list")
                self.messageBox.exec()
                msg = self.DB.add_item(self.models_list["apps"].objectName(), file_name, selected_file[0])

            self.update_from_db(msg)

    def add_app(self):
        # Create a folder selection dialog
        selected_app = QFileDialog.getOpenFileName(filter="*.exe")
        if selected_app[0] != "":
            app_name = os.path.basename(selected_app[0])
            msg = self.DB.add_item(self.models_list["apps"].objectName(), app_name, selected_app[0])
            self.update_from_db(msg)

    def rename_item(self):
        items, model, _, _ = self.MethodeSelectedItems()
        old_name = items[0].data()
        self.dialog_rename.lineEdit.setText(old_name)
        save = self.dialog_rename.exec()
        if save:
            new_name = self.dialog_rename.lineEdit.text()
            if new_name != old_name:
                msg = self.DB.change_item_name(model.objectName(), old_name, new_name)
                self.update_from_db(msg)

    def delete_item(self):
        items, model, icon, name = self.MethodeSelectedItems()
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
        items, model , _, _= self.MethodeSelectedItems()

        for itm in items:
            itm_path = self.DB.get_item_path(model.objectName(),itm.data())
            itm_url = QUrl.fromLocalFile(itm_path)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def open_item_dir(self):
        items, model, _, _ = self.MethodeSelectedItems()
        for itm in items:
            itm_path = self.DB.get_item_path(model.objectName(),itm.data())
            itm_dir = os.path.dirname(itm_path)
            itm_url = QUrl.fromLocalFile(itm_dir)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def copy_item_path(self):
        items, model, _, _ = self.MethodeSelectedItems()

        for itm in items:
            itm_path = self.DB.get_item_path(model.objectName(),itm.data())
            if os.path.exists(itm_path):
                self.clipboard.setText(itm_path)
            else:
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()