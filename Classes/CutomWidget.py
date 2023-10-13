from typing import Dict, Any

from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenu, QStatusBar, QLabel, QListView, QMessageBox, QDialog

# from Classes.Manager import DBManager
from Widgets.Dialog_rename import Ui_Dialog_rename


class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        icon = QIcon(u"_internal/Static/link.png")
        self.setWindowIcon(icon)
        self.setStyleSheet("""
        *{ 
            button-layout: Center;
            color:#fff;
            background-color:rgb(79,79,79)
        }
        QPushButton:hover { 
            background-color: rgb(47, 47, 47); 
        }
        QPushButton{
            margin-left: auto; 
            margin-right: auto;
            border: 1px solid rgb(143, 143, 143);
            border-radius: 5px;
            padding:8px;
        }
        """)

    def set_warning(self, message):
        self.setText(message)
        self.setIcon(QMessageBox.Icon.Warning)
        self.setWindowTitle("Warning")

    def set_error(self, message):
        self.setText(message)
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle("Error")

    def set_info(self, message):
        self.setText(message)
        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle("Information")


class Rename_Dialog(QDialog, Ui_Dialog_rename):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Connect your button signals to functions here
        self.button_save.clicked.connect(self.accept)
        self.button_cancel.clicked.connect(self.reject)


class StatusBar():
    def __init__(self, statusbar: QStatusBar):
        self.statusbar = statusbar
        self.path_label = QLabel()
        self.path_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.statusbar.addPermanentWidget(self.path_label)

    def set_message(self, message):
        self.path_label.setText(message)

    def set_status(self, message):
        self.statusbar.showMessage(message)


class ContextMenu(QMenu):
    contextmenuObject:QObject

    def __init__(self, actions: Dict[str, Any]):
        super().__init__(None)

        self.setObjectName("context_menu")
        # self.actions = actions
        for name, action in actions.items():
            self.addAction(f"{name}", action)

        # self.setStyleSheet("""
        # #context_menu::item:hover {
        # background-color: rgb(120, 120, 120);}
        # """)

    def show_contextMenu_position(self, position, sender: QListView):
        # Get the index of the selected item
        self.contextmenuObject = sender
        selected_index = sender.indexAt(position)
        if selected_index.isValid():
            self.exec(sender.mapToGlobal(position))
    def show_contextMenu(self, position, sender:Any):
        self.contextmenuObject = sender
        self.exec(sender.mapToGlobal(position))

