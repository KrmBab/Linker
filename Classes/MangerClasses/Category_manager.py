from typing import Any

from PySide6.QtWidgets import QComboBox

from Classes.CutomWidget import MessageBox, Category_Dialog, Rename_Dialog
from Classes.Data_center import Data_center


class CategoryManager:
    category_tabe: QComboBox
    dataCenter: Data_center
    messageBox: MessageBox
    category_dialog: Category_Dialog
    dialog_rename: Rename_Dialog
    Get_selectedItems: Any

    def remove_category(self):

        msg = self.dataCenter.dataBase.remove_class(self.category_tabe.objectName(), self.category_dialog.get_class())
        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        else:
            self.category_dialog.rest_items()
            class_items = self.dataCenter.dataBase.get_class(self.category_tabe.objectName())
            self.category_dialog.update_items(class_items)
            # self.update_class_fromDB()

    def add_category(self):

        self.dialog_rename.lineEdit.setText("")
        save = self.dialog_rename.exec()
        if save:
            class_name = self.dialog_rename.lineEdit.text()
            msg = self.dataCenter.dataBase.add_class(self.category_tabe.objectName(), class_name)
            if msg is not None:
                self.messageBox.set_error(msg)
                self.messageBox.exec()
            else:
                self.category_dialog.rest_items()
                class_items = self.dataCenter.dataBase.get_class(self.category_tabe.objectName())
                self.category_dialog.update_items(class_items)
                # self.update_class_fromDB()

    def update_category_fromDB(self):
        for cls in self.dataCenter.models_dict.values():
            cls["class"].clear()
            cls["class"].addItem("All")
            cls["class"].addItems(self.dataCenter.dataBase.get_class(cls["class"].objectName()))

    def add_toClass(self):
        items, model, _, _ = self.Get_selectedItems()

        for mdl in self.dataCenter.models_dict.values():
            if mdl["model"] == model:
                self.category_tabe = mdl["class"]
                break

        class_items = self.dataCenter.dataBase.get_class(self.category_tabe.objectName())
        self.category_dialog.update_items(class_items)
        add = self.category_dialog.exec()
        className = self.category_dialog.get_class()
        self.category_dialog.rest_items()

        if add:
            self.dataCenter.dataBase.set_class(model.objectName(), items[0].data(), className)

        self.update_category_fromDB()
