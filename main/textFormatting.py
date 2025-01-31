from PySide6.QtGui import QTextCursor, QTextBlockFormat, QTextCharFormat
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

def align_left(textEdit):
    # Выравнивание по левому краю
    cursor = textEdit.textCursor()
    block_format = cursor.blockFormat()
    block_format.setAlignment(Qt.AlignLeft)
    cursor.mergeBlockFormat(block_format)
    textEdit.setTextCursor(cursor)

def align_center(textEdit):
    # Выравнивание по центру
    cursor = textEdit.textCursor()
    block_format = cursor.blockFormat()
    block_format.setAlignment(Qt.AlignCenter)
    cursor.mergeBlockFormat(block_format)
    textEdit.setTextCursor(cursor)

def align_right(textEdit):
    # Выравнивание по правому краю
    cursor = textEdit.textCursor()
    block_format = cursor.blockFormat()
    block_format.setAlignment(Qt.AlignRight)
    cursor.mergeBlockFormat(block_format)
    textEdit.setTextCursor(cursor)

def align_justify(textEdit):
    # Выравнивание по ширине
    cursor = textEdit.textCursor()
    block_format = cursor.blockFormat()
    block_format.setAlignment(Qt.AlignJustify)
    cursor.mergeBlockFormat(block_format)
    textEdit.setTextCursor(cursor)

def set_margin(textEdit):
    # Объединённая функция для установки отступов
    options = ["Левый отступ", "Правый отступ"]
    margin_type, ok_type = QInputDialog.getItem(
        textEdit,  # Родительское окно
        "Выбор отступа",  # Заголовок окна
        "Какой отступ вы хотите изменить?",  # Текст сообщения
        options,  # Список вариантов
        editable=False  # Пользователь не может редактировать варианты
    )
    
    if ok_type:
        # Запрашиваем величину отступа
        margin_value, ok_value = QInputDialog.getInt(
            textEdit,  # Родительское окно
            f"Установить {margin_type.lower()}",  # Заголовок окна
            "Введите отступ (в пикселях):",  # Сообщение
            0,  # Значение по умолчанию
            0,  # Минимальное значение
            100  # Максимальное значение
        )

        if ok_value:
            cursor = textEdit.textCursor()
            block_format = QTextBlockFormat()

            if margin_type == "Левый отступ":
                block_format.setLeftMargin(margin_value)
            elif margin_type == "Правый отступ":
                block_format.setRightMargin(margin_value)

            cursor.mergeBlockFormat(block_format)
            textEdit.setTextCursor(cursor)

def set_line_spacing(textEdit):
    # Установка междустрочного интервала
    spacing, ok = QInputDialog.getDouble(
        textEdit,  # Родительское окно
        "Междустрочный интервал",  # Заголовок окна
        "Введите интервал (например, 1.0, 1.5, 2.0):",  # Сообщение
        0.1,  # Значение по умолчанию
        0.1,  # Минимальное значение
        3.0,  # Максимальное значение
        1  # Количество знаков после запятой
    )
    if ok:
        cursor = textEdit.textCursor()
        block_format = cursor.blockFormat()
        
        # Устанавливаем междустрочный интервал с типом LineDistanceHeight (3)
        block_format.setLineHeight(spacing * 100, 3)  # 3 соответствует LineDistanceHeight
        
        cursor.mergeBlockFormat(block_format)
        textEdit.setTextCursor(cursor)


def setBold(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    textEdit.setTextCursor(cursor)

    # Создаем новый формат
    newFormat = cursor.charFormat()
    newFormat.setFontWeight(700 if newFormat.fontWeight() != 700 else 400)

    # Применяем формат ко всему выделенному диапазону
    cursor.mergeCharFormat(newFormat)
    


def setLink(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    textEdit.setTextCursor(cursor)

    # Узнаем ссылку от пользователя
    text, ok = QInputDialog.getText(textEdit, "Вставить ссылку", "Введите Ссылку:")
    if not ok:
        return

    # Создаем новый формат
    oldFormat = cursor.charFormat()
    newFormat = cursor.charFormat()

    newFormat.setAnchor(True)
    newFormat.setAnchorHref(text)
    newFormat.setForeground(Qt.blue)
    newFormat.setFontUnderline(True)
    if cursor.hasSelection():
        # Применяем формат ко всему выделенному диапазону
        cursor.setCharFormat(newFormat)
        cursor.clearSelection()
        textEdit.setTextCursor(cursor)
    else:
        cursor.insertText(text, newFormat)

    # Сбрасываем стиль на тот что был до этого
    cursor.setCharFormat( oldFormat )
    textEdit.setTextCursor(cursor)
    

def setItalic(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    textEdit.setTextCursor(cursor)

    newFormat = cursor.charFormat()
    newFormat.setFontItalic( not newFormat.fontItalic() )

    cursor.mergeCharFormat(newFormat)

def setUnderlined(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    textEdit.setTextCursor(cursor)

    newFormat = cursor.charFormat()
    newFormat.setFontUnderline( not newFormat.fontUnderline() )


    cursor.mergeCharFormat(newFormat)

def clearStyles(textEdit):
    cursor = textEdit.textCursor()
    selectionStart = cursor.selectionStart()
    selectionEnd = cursor.selectionEnd()

    cursor.setPosition(selectionStart)
    cursor.setPosition(selectionEnd, QTextCursor.MoveMode.KeepAnchor)
    textEdit.setTextCursor(cursor)

    # Создаём чистый формат без стилей
    currentFormat = cursor.charFormat()
    clearFormat = QTextCharFormat()
    clearFormat.setFontFamilies( currentFormat.fontFamilies() )
    clearFormat.setFontPointSize( currentFormat.fontPointSize() )
    cursor.setCharFormat(clearFormat)  # Сбрасываем форматирование

    # textEdit.setTextCursor(cursor)