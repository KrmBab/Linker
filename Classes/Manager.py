import os

from PySide6.QtCore import QFileInfo
from PySide6.QtWidgets import QFileIconProvider, QApplication

from .CutomWidget import MessageBox, Rename_Dialog
from .DataCenter import DataCenter, ManagerMethods
from .MangerClasses import ItemManager, Category_Dialog, Category_Menu


class Manager(ItemManager):

    def __init__(self, dataCenter: DataCenter):
        self.dataCenter = dataCenter

        self.manger_methods = ManagerMethods(get_selectedItems=self.get_selectedItems,
                                             update_status=self.update_status)

        self.dialog_rename = Rename_Dialog(self)

        self.category_dialog = Category_Dialog(dataCenter, self)
        self.category_menu = Category_Menu(dataCenter, self)

        self.messageBox = MessageBox(self)
        self.clipboard = QApplication.clipboard()

    def get_selectedItems(self):
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
        items, model, label_icon, label_name = self.get_selectedItems()
        if items:
            path = self.dataCenter.dataBase.get_item_path(model.objectName(), items[0].data())
            self.dataCenter.statusbar.set_message(f"{path}")

            label_icon.setPixmap(self.get_exe_icon(path))
            label_name.setText(os.path.basename(path))

    def update_category_fromDB(self):
        for cls in self.dataCenter.models_dict.values():
            cls["class"].clear()
            cls["class"].addItem("All")
            cls["class"].addItems(self.dataCenter.dataBase.get_class(cls["class"].objectName()))