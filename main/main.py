import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from views.ui_main import Ui_MainWindow 
from utils import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Настройка TextEdit
        self.ui.textEdit.setPlaceholderText("Здесь пустовато...")
        setSize(self.ui.textEdit, self.ui.FontSize.value())
        changeFont(self.ui.textEdit, self.ui.FontBox)
        self.hasChanged = False
        self.outputPath = None
        self.ui.saveDocAction.setDisabled(True)

        # Всякие коннекты к функциям
        self.ui.BoldStyleButton.clicked.connect(lambda: setBold(self.ui.textEdit))
        self.ui.ItalicStyleButton.clicked.connect(lambda: setItalic(self.ui.textEdit))
        self.ui.UnderlineStyleButton.clicked.connect(lambda: setUnderlined(self.ui.textEdit))
        self.ui.clearButton.clicked.connect(lambda: clearStyles(self.ui.textEdit))
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
        self.ui.LinkButton.clicked.connect(lambda: setLink(self.ui.textEdit))

        self.ui.imageAction.triggered.connect( self.loadImage )
        self.ui.linkAction.triggered.connect(lambda: setLink(self.ui.textEdit))
        self.ui.createDocAction.triggered.connect( self.newDocument )
        self.ui.textEdit.textChanged.connect( self.OnChange )
        self.ui.saveDocAction.triggered.connect( self.saveDocument )
        self.ui.openDocAction.triggered.connect( self.openDocument )
    
    def newDocument(self):
        self.ui.textEdit.clear()
        self.hasChanged = False
        self.outputPath = None
        self.ui.saveDocAction.setDisabled(True)
    
    # Для Сохранения
    def OnChange(self):
        self.hasChanged = True
        if len( self.ui.textEdit.toPlainText() ) != 0:
            self.ui.saveDocAction.setDisabled(False)
        else:
            self.ui.saveDocAction.setDisabled(True)
    
    def saveDocument(self):
        savePath, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if savePath:
            with open(savePath, 'w', encoding='utf-8') as file:
                file.write( self.ui.textEdit.toHtml() )
                self.ui.saveDocAction.setDisabled(True)

    # Для открытия
    def openDocument(self):
        loadPath, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if loadPath:
            self.newDocument()
            with open(loadPath, 'r', encoding='utf-8') as file:
                text = file.read()
                self.ui.textEdit.setHtml( text )


    # Загрузка изображений и их вставка
    def loadImage(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Image", '', "Images (*.png *.jpg *.bmp *.svg)")
        if file:
            image_format = QTextImageFormat()
            image_format.setName(file)
            self.ui.textEdit.textCursor().insertImage(image_format)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec())