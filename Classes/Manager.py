import os

from PySide6.QtCore import QFileInfo
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileIconProvider, QApplication, QListView, QLabel

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

    def get_selectedItems(self) -> (QListView.selectedIndexes, QListView.model, QLabel, QLabel):
        '''
        this function checks te listViews and returns the selected item info from dataCenter.listsViews_dict
        :return: item info
            - QListView.selectedIndexes : selected index from QlistView
            - QListView.model : model of the QlistView
            - QLabel : icon label
            - QLabel : path label
        '''
        for LV in self.dataCenter.listsViews_dict:
            items = LV["list"].selectedIndexes()
            if items:
                return items, LV["list"].model(), LV["icon"], LV["path"]
        return None, None, None, None

    def get_exe_icon(self, exe_path) -> QIcon:
        '''
        this function return the QIcon of the file
        :param exe_path: file path
        :return: QIcon : the icon of the file
        '''
        icon_provider = QFileIconProvider()
        file_info = QFileInfo(exe_path)
        icon = icon_provider.icon(file_info)
        icon = icon.pixmap(30, 30)
        return icon

    def update_status(self):
        '''
        this function count the listeViews items and update the statusbar
        :return:
        '''
        filesCount = self.dataCenter.models_dict["files"]["model"].rowCount()
        foldersCount = self.dataCenter.models_dict["folders"]["model"].rowCount()
        appsCount = self.dataCenter.models_dict["apps"]["model"].rowCount()

        self.dataCenter.statusbar.set_status(f"Apps : {appsCount} | Files : {filesCount} | Folders : "
                                             f"{foldersCount}")

    def show_path_and_icon(self):
        '''
        this function update the icon and path label with information of selected item in the listView
        :return:
        '''
        items, model, label_icon, label_name = self.get_selectedItems()
        if items:
            path = self.dataCenter.dataBase.get_item_path(model.objectName(), items[0].data())
            self.dataCenter.statusbar.set_message(f"{path}")

            label_icon.setPixmap(self.get_exe_icon(path))
            label_name.setText(os.path.basename(path))

    def update_category_fromDB(self):
        '''
        this function gets item from db according to it category name than update the listeview
        :return:
        '''
        for cls in self.dataCenter.models_dict.values():
            cls["class"].clear()
            cls["class"].addItem("All")
            cls["class"].addItems(self.dataCenter.dataBase.get_class(cls["class"].objectName()))