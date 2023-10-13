import os

import win32com.client
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QComboBox, QApplication, QFileDialog

from Classes.CutomWidget import MessageBox, Rename_Dialog
from Classes.DataCenter import DataCenter, ManagerMethods
from Classes.MangerClasses.Widget_interface import Category_Dialog


class ItemManager:
    category_tabe: QComboBox
    dataCenter: DataCenter
    messageBox: MessageBox
    category_dialog: Category_Dialog
    dialog_rename: Rename_Dialog
    clipboard: QApplication.clipboard
    
    manger_methods:ManagerMethods


    # region item_manip
    def rename_item(self):
        items, model, _, _ = self.manger_methods.get_selectedItems()
        old_name = items[0].data()
        new_name = self.dialog_rename.show_window(old_name)
        if new_name is not None:
            msg = self.dataCenter.dataBase.change_item_name(model.objectName(), old_name, new_name)
            self.update_from_db(msg)

    def delete_item(self):
        items, model, icon, name = self.manger_methods.get_selectedItems()
        icon.setPixmap(QPixmap())
        name.setText("")
        self.dataCenter.statusbar.set_message("")
        if items:
            msg = None
            for itm in items:
                msg = self.dataCenter.dataBase.delete_item(model.objectName(), itm.data())
            self.update_from_db(msg)
            self.manger_methods.update_status()

    def open_item(self):
        items, model, _, _ = self.manger_methods.get_selectedItems()

        for itm in items:
            itm_path = self.dataCenter.dataBase.get_item_path(model.objectName(), itm.data())
            itm_url = QUrl.fromLocalFile(itm_path)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                

    def open_item_dir(self):
        items, model, _, _ = self.manger_methods.get_selectedItems()
        for itm in items:
            itm_path = self.dataCenter.dataBase.get_item_path(model.objectName(), itm.data())
            itm_dir = os.path.dirname(itm_path)
            itm_url = QUrl.fromLocalFile(itm_dir)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                

    def copy_item_path(self):
        items, model, _, _ = self.manger_methods.get_selectedItems()

        for itm in items:
            itm_path = self.dataCenter.dataBase.get_item_path(model.objectName(), itm.data())
            if os.path.exists(itm_path):
                self.clipboard.setText(itm_path)
            else:
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                

    # endregion

    # region add_item
    def add_folder(self):
        # Create a folder selection dialog
        selected_folder = QFileDialog.getExistingDirectory()
        if selected_folder != "":
            folder_name = os.path.basename(selected_folder)
            msg = self.dataCenter.dataBase.add_item(self.dataCenter.models_dict["folders"]["model"].objectName(),
                                                    folder_name, selected_folder)
            self.update_from_db(msg)

    def add_file(self):
        # Create a folder selection dialog
        file_path = QFileDialog.getOpenFileName()[0]
        if file_path != "":
            if ".lnk" in file_path:
                shell = win32com.client.Dispatch("WScript.Shell")
                file_path = shell.CreateShortCut(file_path).Targetpath
            file_name = os.path.basename(file_path)

            if ".exe" not in file_name:
                msg = self.dataCenter.dataBase.add_item(self.dataCenter.models_dict["files"]["model"].objectName(),
                                                        file_name, file_path)

            else:
                # Show the warning message box and wait for user interaction
                self.messageBox.set_warning("This is an .exe file it will be add to Apps list")
                
                msg = self.dataCenter.dataBase.add_item(self.dataCenter.models_dict["apps"]["model"].objectName(),
                                                        file_name, file_path)

            self.update_from_db(msg)

    def add_app(self):
        # Create a folder selection dialog
        selected_app = QFileDialog.getOpenFileName(filter="*.exe")
        if selected_app[0] != "":
            app_name = os.path.basename(selected_app[0])
            msg = self.dataCenter.dataBase.add_item(self.dataCenter.models_dict["apps"]["model"].objectName(), app_name,
                                                    selected_app[0])
            self.update_from_db(msg)

    # endregion

    # region update_fromDB

    def update_from_db(self, msg: str = None):

        if msg is not None:
            self.messageBox.set_error(msg)
            
        for model in self.dataCenter.models_dict.values():
            model["model"].setStringList(
                self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def update_apps_fromDB(self):
        model = self.dataCenter.models_dict["apps"]
        model["model"].setStringList(
            self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))
        self.manger_methods.update_status()

    def update_folders_fromDB(self):
        model = self.dataCenter.models_dict["folders"]
        model["model"].setStringList(
            self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))
        self.manger_methods.update_status()

    def update_files_fromDB(self):
        model = self.dataCenter.models_dict["files"]
        model["model"].setStringList(
            self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))
        self.manger_methods.update_status()

    # endregion
