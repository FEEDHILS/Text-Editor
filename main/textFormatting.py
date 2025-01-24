from PySide6.QtGui import QTextCursor

def setBold(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    # Создаем новый формат
    newFormat = cursor.charFormat()
    newFormat.setFontWeight(700 if newFormat.fontWeight() != 700 else 400)

    # Применяем формат ко всему выделенному диапазону
    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    cursor.mergeCharFormat(newFormat)
    textEdit.setTextCursor(cursor)
    

def setItalic(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    newFormat = cursor.charFormat()
    newFormat.setFontItalic( not newFormat.fontItalic() )

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    cursor.mergeCharFormat(newFormat)
    textEdit.setTextCursor(cursor)

def setUnderlined(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    newFormat = cursor.charFormat()
    newFormat.setFontUnderline( not newFormat.fontUnderline() )

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    cursor.mergeCharFormat(newFormat)
    textEdit.setTextCursor(cursor)