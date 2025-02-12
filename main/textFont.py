from PySide6.QtWidgets import QFontComboBox, QColorDialog
from PySide6.QtGui import QTextCursor, QTextCharFormat, QTextImageFormat

def changeFont(textEdit, fontBox):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()


    newFormat = cursor.charFormat()
    font = fontBox.currentFont()
    font.setPointSize( newFormat.fontPointSize() )
    newFormat.setFont( font )

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    
    cursor.mergeCharFormat(newFormat)
    textEdit.setTextCursor(cursor)

def setSize(textEdit, size):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()


    newFormat = QTextCharFormat()
    newFormat.setFontPointSize( size )

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    
    cursor.mergeCharFormat(newFormat)
    textEdit.setTextCursor(cursor)

# Изменение спинбокса(окошко с размером шрифта) в зависимости от выделенного текста
# def fontSizeUpdate(textEdit, size):
#     cursor = textEdit.textCursor()
#     if cursor.selectionStart() == cursor.selectionEnd():
#         return

#     format = cursor.charFormat()
#     print(format.fontPointSize(), cursor.selectedText(), textEdit.font().pointSize())
#     size.setValue( format.fontPointSize() )

def change_text_color(textEdit):
    # Изменение цвета текста
    color = QColorDialog.getColor()
    if color.isValid():
        cursor = textEdit.textCursor()
        if cursor.hasSelection():
            fmt = QTextCharFormat()
            fmt.setForeground(color)
            cursor.mergeCharFormat(fmt)

def change_background_color(textEdit):
    # Изменение цвета фона текста
    color = QColorDialog.getColor()
    if color.isValid():
        cursor = textEdit.textCursor()
        if cursor.hasSelection():
            fmt = QTextCharFormat()
            fmt.setBackground(color)
            cursor.mergeCharFormat(fmt)
