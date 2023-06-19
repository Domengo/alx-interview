import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QDoubleSpinBox, QWidget, QFormLayout, QLineEdit, QPushButton


def getDoubleSpinBox() -> QDoubleSpinBox:
    box = QDoubleSpinBox()
    box.setMinimum(float("-inf"))
    box.setMaximum(float("inf"))
    box.setSingleStep(0.05)
    box.setValue(100)
    return box


def getLineEdit(placehoder: str, password: bool = False):
    lineEdit = QLineEdit()
    lineEdit.setPlaceholderText(placehoder)
    if password:
        lineEdit.setEchoMode(QLineEdit.Password)
    return lineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Open Bank")
        self.widget = QWidget()
        self.widgetLayout = QFormLayout()
        self.widgetLayout.addRow("ID", getLineEdit(placehoder="Investor name"))
        self.widgetLayout.addRow("Investment", getDoubleSpinBox())
        self.widgetLayout.addRow("Password", getLineEdit(placehoder="Enter secret password", password=True))
        self.widgetLayout.addRow(QPushButton("Invest"), QPushButton("Cancel"))
        self.widget.setLayout(self.widgetLayout)
        self.setCentralWidget(self.widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())