import sys

from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.load.clicked.connect(self.checkNumber)
        self.show()

    def checkNumber(self):
        file_name = QFileDialog().getOpenFileName(self, "Wybierz", ".", "*.txt")
        if file_name != '':
            with open(file_name, "r") as file:
                file.write(self.ui.numbers.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())