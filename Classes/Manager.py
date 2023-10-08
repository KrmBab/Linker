import os
from dataclasses import dataclass
from typing import Dict, Union

from PySide6.QtCore import QUrl, QFileInfo, QStringListModel
from PySide6.QtGui import QDesktopServices, QPixmap, QIcon
from PySide6.QtWidgets import QFileDialog, QFileIconProvider, QApplication, QComboBox, QListView, QLabel

from .CutomWidget import MessageBox, Rename_Dialog, Category_Dialog, StatusBar
from .DataBase import DataBase


@dataclass
class Data_center:
    iconLinker: QIcon
    models_dict: Dict[str, Union[Dict[str, QStringListModel], Dict[str, QComboBox]]]
    listsViews_dict: [Dict[str, QListView], Dict[str, QLabel], Dict[str, QLabel]]
    dataBase: DataBase
    statusbar: StatusBar


class Manager():
    __category_tabe = None

    def __init__(self, dataCenter: Data_center):
        self.dataCenter = dataCenter

        self.dialog_rename = Rename_Dialog()
        self.dialog_rename.setWindowIcon(self.dataCenter.iconLinker)
        self.category_dialog = Category_Dialog(self.add_class, self.remove_class)
        self.category_dialog.setWindowIcon(self.dataCenter.iconLinker)

        self.messageBox = MessageBox()
        self.clipboard = QApplication.clipboard()

    # region class_manip
    def remove_class(self):

        msg = self.dataCenter.dataBase.remove_class(self.__category_tabe.objectName(), self.category_dialog.get_class())
        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        else:
            self.category_dialog.rest_items()
            class_items = self.dataCenter.dataBase.get_class(self.__category_tabe.objectName())
            self.category_dialog.update_items(class_items)
            # self.update_class_fromDB()

    def add_class(self):

        self.dialog_rename.lineEdit.setText("")
        save = self.dialog_rename.exec()
        if save:
            class_name = self.dialog_rename.lineEdit.text()
            msg = self.dataCenter.dataBase.add_class(self.__category_tabe.objectName(), class_name)
            if msg is not None:
                self.messageBox.set_error(msg)
                self.messageBox.exec()
            else:
                self.category_dialog.rest_items()
                class_items = self.dataCenter.dataBase.get_class(self.__category_tabe.objectName())
                self.category_dialog.update_items(class_items)
                # self.update_class_fromDB()

    def update_class_fromDB(self):
        for cls in self.dataCenter.models_dict.values():
            cls["class"].clear()
            cls["class"].addItem("All")
            cls["class"].addItems(self.dataCenter.dataBase.get_class(cls["class"].objectName()))
        pass

    # endregion

    # region other_actions
    def Get_selectedItems(self):
        for LV in self.dataCenter.listsViews_dict:
            items = LV["list"].selectedIndexes()
            if items:
                return items, LV["list"].model(), LV["icon"], LV["path"]
        return None, None, None, None

    def get_exe_icon(self, exe_path):
        icon_provider = QFileIconProvider()
        file_info = QFileInfo(exe_path)
        icon = icon_provider.icon(file_info)
        icon = icon.pixmap(30, 30)
        return icon

    def update_status(self):
        filesCount = self.dataCenter.models_dict["files"]["model"].rowCount()
        foldersCount = self.dataCenter.models_dict["folders"]["model"].rowCount()
        appsCount = self.dataCenter.models_dict["apps"]["model"].rowCount()

        self.dataCenter.statusbar.set_status(f"Apps : {appsCount} | Files : {filesCount} | Folders : "
                                             f"{foldersCount}")

    def show_path(self):
        items, model, label_icon, label_name = self.Get_selectedItems()
        if items:
            path = self.dataCenter.dataBase.get_item_path(model.objectName(), items[0].data())
            self.dataCenter.statusbar.set_message(f"{path}")

            label_icon.setPixmap(self.get_exe_icon(path))
            label_name.setText(os.path.basename(path))

    # endregion

    # region update_fromDB
    def update_from_db(self, msg: str = None):

        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        for model in self.dataCenter.models_dict.values():
            model["model"].setStringList(
                self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def update_apps_fromDB(self):
        model = self.dataCenter.models_dict["apps"]
        model["model"].setStringList(
            self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))
        self.update_status()

    def update_folders_fromDB(self):
        model = self.dataCenter.models_dict["folders"]
        model["model"].setStringList(
            self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))

    def update_files_fromDB(self):
        model = self.dataCenter.models_dict["files"]
        model["model"].setStringList(
            self.dataCenter.dataBase.get_all_names(model["model"].objectName(), model["class"].currentText()))

    # endregion

    # region add_items
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
        selected_file = QFileDialog.getOpenFileName()
        if selected_file[0] != "":
            file_name = os.path.basename(selected_file[0])

            if ".exe" not in file_name:
                msg = self.dataCenter.dataBase.add_item(self.dataCenter.models_dict["files"]["model"].objectName(),
                                                        file_name, selected_file[0])

            else:
                # Show the warning message box and wait for user interaction
                self.messageBox.set_warning("This is an .exe file it will be add to Apps list")
                self.messageBox.exec()
                msg = self.dataCenter.dataBase.add_item(self.dataCenter.models_dict["apps"]["model"].objectName(),
                                                        file_name, selected_file[0])

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

    # region item_manip
    def rename_item(self):
        items, model, _, _ = self.Get_selectedItems()
        old_name = items[0].data()
        self.dialog_rename.lineEdit.setText(old_name)
        save = self.dialog_rename.exec()
        if save:
            new_name = self.dialog_rename.lineEdit.text()
            if new_name != old_name:
                msg = self.dataCenter.dataBase.change_item_name(model.objectName(), old_name, new_name)
                self.update_from_db(msg)

    def delete_item(self):
        items, model, icon, name = self.Get_selectedItems()
        icon.setPixmap(QPixmap())
        name.setText("")
        self.dataCenter.statusbar.set_message("")
        if items:
            msg = None
            for itm in items:
                msg = self.dataCenter.dataBase.delete_item(model.objectName(), itm.data())
            self.update_from_db(msg)
            self.update_status()

    def open_item(self):
        items, model, _, _ = self.Get_selectedItems()

        for itm in items:
            itm_path = self.dataCenter.dataBase.get_item_path(model.objectName(), itm.data())
            itm_url = QUrl.fromLocalFile(itm_path)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def open_item_dir(self):
        items, model, _, _ = self.Get_selectedItems()
        for itm in items:
            itm_path = self.dataCenter.dataBase.get_item_path(model.objectName(), itm.data())
            itm_dir = os.path.dirname(itm_path)
            itm_url = QUrl.fromLocalFile(itm_dir)
            if not QDesktopServices.openUrl(itm_url):
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def copy_item_path(self):
        items, model, _, _ = self.Get_selectedItems()

        for itm in items:
            itm_path = self.dataCenter.dataBase.get_item_path(model.objectName(), itm.data())
            if os.path.exists(itm_path):
                self.clipboard.setText(itm_path)
            else:
                self.messageBox.set_error(f"Error: Failed to open {itm.data()} on '{itm_path}'")
                self.messageBox.exec()

    def add_toClass(self):
        items, model, _, _ = self.Get_selectedItems()

        for mdl in self.dataCenter.models_dict.values():
            if mdl["model"] == model:
                self.__category_tabe = mdl["class"]
                break

        class_items = self.dataCenter.dataBase.get_class(self.__category_tabe.objectName())
        self.category_dialog.update_items(class_items)
        add = self.category_dialog.exec()
        className = self.category_dialog.get_class()
        self.category_dialog.rest_items()

        if add:
            self.dataCenter.dataBase.set_class(model.objectName(), items[0].data(), className)

        self.update_class_fromDB()

    # endregion
    def __end(self):
        pass
