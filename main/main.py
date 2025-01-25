import sys
from PySide6 import QtCore
from PySide6.QtWidgets import *
from views.ui_main import Ui_MainWindow 
from textFormatting import *
from textFont import *
from ImageHandler import *
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        setSize(self.ui.textEdit, 12)
        # Всякие коннекты к функциям
        self.ui.BoldStyleButton.clicked.connect(lambda: setBold(self.ui.textEdit))
        self.ui.ItalicStyleButton.clicked.connect(lambda: setItalic(self.ui.textEdit))
        self.ui.UnderlineStyleButton.clicked.connect(lambda: setUnderlined(self.ui.textEdit))
        self.ui.FontBox.currentFontChanged.connect(lambda: changeFont(self.ui.textEdit, 
                                                                      self.ui.FontBox))
        self.ui.FontSize.valueChanged.connect(lambda: setSize(self.ui.textEdit, 
                                                              self.ui.FontSize.value()))
        
        self.ui.ImageButton.clicked.connect( self.loadImage )
        self.ui.LAlignButton.clicked.connect(lambda: align_left(self.ui.textEdit))
        self.ui.CAlignButton.clicked.connect(lambda: align_center(self.ui.textEdit))
        self.ui.RAlignButton.clicked.connect(lambda: align_right(self.ui.textEdit))
        self.ui.WAlignButton.clicked.connect(lambda: align_justify(self.ui.textEdit))
        self.ui.ChangeText.clicked.connect(lambda: change_text_color(self.ui.textEdit))
        self.ui.ChangeBack.clicked.connect(lambda: change_background_color(self.ui.textEdit))
        self.ui.ChangeMargin.clicked.connect(lambda: set_margin(self.ui.textEdit))
        self.ui.LineSpace.clicked.connect(lambda: set_line_spacing(self.ui.textEdit))


        # self.ui.textEdit.cursorPositionChanged.connect(lambda: fontSizeUpdate(self.ui.textEdit,
        #                                                                  self.ui.FontSize))
        # self.ui.textEdit.cursorPositionChanged.connect(lambda: CursorPositionChanged(self.ui.textEdit))
        # cursor = self.ui.textEdit.textCursor()
        # image_format = QTextImageFormat()
        # image_format.setName("sosaker.jpg")
        # image_format.setWidth(128)
        # image_format.setHeight(128)
        # cursor.insertImage(image_format)
    def loadImage(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Image", '', "Images (*.png *.jpg *.bmp *.svg)")
        if file:
            image_format = QTextImageFormat()
            image_format.setName(file)
            self.ui.textEdit.textCursor().insertImage(image_format)



        

    def resizeEvent(self, event):
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec())