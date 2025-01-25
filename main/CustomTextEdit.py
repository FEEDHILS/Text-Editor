from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, Qt, QDesktopServices
from ImageHandler import ImageResizeDialog

class CustomTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def contextMenuEvent(self, event):
        # Получаем стандартное контекстное меню QTextEdit
        menu = self.createStandardContextMenu()

        # Создаем свои действия (опции)
        self.cursor = self.textCursor()
        self.format = self.cursor.charFormat()
        ImageSizeOption = QAction("Изменить размер Изображения", self)
        ImageSizeOption.triggered.connect(self.ImageResize)
        if not self.format.isImageFormat() or self.cursor.selectionStart() == self.cursor.selectionEnd():
            ImageSizeOption.setDisabled(True)

        # TODO: Доделать это дерьмо!!!
        InsertLinkOption = QAction("Вставить ссылку", self)
        InsertLinkOption.triggered.connect(self.InsertLink)
        InsertLinkOption.setDisabled(True)

        # Добавляем их в меню
        menu.addSeparator()  # Разделитель между стандартными и новыми опциями
        menu.addAction(ImageSizeOption)
        menu.addAction(InsertLinkOption)

        # Показываем контекстное меню
        menu.exec(event.globalPos())

    def ImageResize(self):
        image = self.format.toImageFormat()
        dialog = ImageResizeDialog( image.width(), image.height() )
        if dialog.exec() == QDialog.Accepted:  # Проверяем, был ли диалог принят
            width = dialog.get_width()
            height = dialog.get_height()
            image.setWidth(width)
            image.setHeight(height)
            self.cursor.mergeCharFormat(image)

    def InsertLink(self):
        self.insertPlainText("Вы выбрали опцию 2!\n")

    # По умолчанию QTextEdit не поддерживает гиперссылки, поэтому далее идет немного кастомной реализации

    # Меняем курсор при наведении на ссылку
    def mouseMoveEvent(self, e):
        self.anchor = self.anchorAt(e.pos())
        if self.anchor:
            self.viewport().setCursor( Qt.CursorShape.PointingHandCursor )
        else:
            self.viewport().unsetCursor()
        
        super().mouseMoveEvent(e)
    
    def mouseDoubleClickEvent(self, e):
        self.anchor = self.anchorAt(e.pos())
        self.current_link = self.textCursor().charFormat().anchorHref()
        QDesktopServices.openUrl(self.current_link)
        return super().mouseDoubleClickEvent(e)
    
        