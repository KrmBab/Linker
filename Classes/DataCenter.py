from dataclasses import dataclass
from typing import Dict, Union, Any

from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QComboBox, QListView, QLabel

from Classes.CutomWidget import StatusBar
from Classes.DataBase import DataBase


@dataclass
class DataCenter:
    iconLinker: QIcon
    models_dict: Dict[str, Union[Dict[str, QStringListModel], Dict[str, QComboBox]]]
    listsViews_dict: [Dict[str, QListView], Dict[str, QLabel], Dict[str, QLabel]]
    dataBase: DataBase
    statusbar: StatusBar

@dataclass
class ManagerMethods:
    get_selectedItems: Any
    update_status: Any
