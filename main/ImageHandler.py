from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from views.ui_dialog import Ui_Dialog

class ImageResizeDialog(QDialog):
    def __init__(self, width, height):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Изменить размеры Изображения: ")
        self.ui.WidthBox.setValue(width)
        self.ui.HeightBox.setValue(height)
        self.ui.SaveButton.clicked.connect(self.accept)

    def get_width(self):
        return self.ui.WidthBox.value()

    def get_height(self):
        return self.ui.HeightBox.value()
    