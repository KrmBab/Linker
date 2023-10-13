from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QDialog, QListView

from Classes.CutomWidget import Rename_Dialog, MessageBox
from Classes.DataCenter import DataCenter
from Widgets.Dialog_CategoryMenu import Ui_Dialog_CategoryMenu
from Widgets.Dialog_addToClass import Ui_Dialog_addToClass


class Category_Dialog(QDialog, Ui_Dialog_addToClass):
    item = None
    class_table:None
    def __init__(self, dataCenter:DataCenter, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dataCenter = dataCenter
        # Connect your button signals to functions here
        self.button_save.clicked.connect(self.accept)
        self.button_cancel.clicked.connect(self.reject)
        self.setWindowIcon(self.dataCenter.iconLinker)

    def accept(self) -> None:

        item_tabl =  self.class_table.objectName()
        message = self.dataCenter.dataBase.set_class(item_tabl,
                                                     self.item.data(), self.class_items.currentText())
        self.close()

    def show_window(self, object:QListView):
        self.item = object.selectedIndexes()[0]
        self.class_table = object.model()
        self.update_category()
        self.exec()

    def update_category(self):
        object_category = self.dataCenter.models_dict[self.class_table.objectName()]["class"]
        items = [object_category.itemText(i) for i in range(object_category.count())]
        self.class_items.clear()
        self.class_items.addItems(items)

    def get_class(self):
        return self.class_items.currentText()


class Category_Menu(QDialog, Ui_Dialog_CategoryMenu):
    dataCenter = None
    object_category = None
    def __init__(self, dataCenter:DataCenter, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dataCenter = dataCenter
        self.model_category = QStringListModel()
        self.listView_category.setModel(self.model_category)

        self.dialog_rename = Rename_Dialog()
        self.messageBox = MessageBox()

        self.button_add.clicked.connect(self.add_category)
        self.button_delete.clicked.connect(self.remove_category)
        # self.button_edit.clicked.connect(edite_method)


    def show_category_menu(self, object):
        self.object_category = object
        self.update_category_items()
        self.exec()

    def update_category_items(self):
        itmes = self.dataCenter.dataBase.get_class(self.object_category.objectName())
        self.model_category.setStringList(itmes)

    def add_category(self):

        self.dialog_rename.lineEdit.setText("")
        save = self.dialog_rename.exec()
        if save:
            class_name = self.dialog_rename.lineEdit.text()
            msg = self.dataCenter.dataBase.add_class(self.object_category.objectName(), class_name)
            if msg is not None:
                self.messageBox.set_error(msg)
                self.messageBox.exec()
            else:
                self.update_category_items()

    def remove_category(self):
        category_name = self.listView_category.selectedIndexes()[0].data()
        msg = self.dataCenter.dataBase.remove_class(self.object_category.objectName(), category_name)
        if msg is not None:
            self.messageBox.set_error(msg)
            self.messageBox.exec()
        else:
            self.update_category_items()

    def closeEvent(self, event):
        self.object_category.clear()
        self.object_category.addItem("All")
        self.object_category.addItems(self.dataCenter.dataBase.get_class(self.object_category.objectName()))