import os

from PySide6.QtCore import QFileInfo
from PySide6.QtWidgets import QFileIconProvider, QApplication

from .CutomWidget import MessageBox, Rename_Dialog, Category_Dialog
from .Data_center import Data_center
from .MangerClasses import CategoryManager, ItemManager


class Manager(CategoryManager, ItemManager):

    def __init__(self, dataCenter: Data_center):
        self.dataCenter = dataCenter

        self.dialog_rename = Rename_Dialog()
        self.dialog_rename.setWindowIcon(self.dataCenter.iconLinker)
        self.category_dialog = Category_Dialog(self.add_category, self.remove_category)
        self.category_dialog.setWindowIcon(self.dataCenter.iconLinker)

        self.messageBox = MessageBox()
        self.clipboard = QApplication.clipboard()

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
