from PySide6.QtWidgets import QApplication

from Classes.MainWindow import Widget, sys, check_single_instance

if __name__ == "__main__":
    check_single_instance()

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
