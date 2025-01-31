# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QFontComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStatusBar,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

from customtextedit import CustomTextEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1021, 739)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.createDocAction = QAction(MainWindow)
        self.createDocAction.setObjectName(u"createDocAction")
        self.imageAction = QAction(MainWindow)
        self.imageAction.setObjectName(u"imageAction")
        self.linkAction = QAction(MainWindow)
        self.linkAction.setObjectName(u"linkAction")
        self.saveDocAction = QAction(MainWindow)
        self.saveDocAction.setObjectName(u"saveDocAction")
        self.openDocAction = QAction(MainWindow)
        self.openDocAction.setObjectName(u"openDocAction")
        self.MainArea = QWidget(MainWindow)
        self.MainArea.setObjectName(u"MainArea")
        self.MainArea.setEnabled(True)
        self.gridLayout = QGridLayout(self.MainArea)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.ToolPanel = QGridLayout()
        self.ToolPanel.setObjectName(u"ToolPanel")
        self.RandomBullshitLayout = QVBoxLayout()
        self.RandomBullshitLayout.setObjectName(u"RandomBullshitLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LinkButton = QToolButton(self.MainArea)
        self.LinkButton.setObjectName(u"LinkButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertLink))
        self.LinkButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.LinkButton)

        self.ImageButton = QToolButton(self.MainArea)
        self.ImageButton.setObjectName(u"ImageButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.CameraPhoto))
        self.ImageButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.ImageButton)

        self.LAlignButton = QToolButton(self.MainArea)
        self.LAlignButton.setObjectName(u"LAlignButton")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyLeft))
        self.LAlignButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.LAlignButton)

        self.CAlignButton = QToolButton(self.MainArea)
        self.CAlignButton.setObjectName(u"CAlignButton")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyCenter))
        self.CAlignButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.CAlignButton)

        self.RAlignButton = QToolButton(self.MainArea)
        self.RAlignButton.setObjectName(u"RAlignButton")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyRight))
        self.RAlignButton.setIcon(icon4)

        self.horizontalLayout.addWidget(self.RAlignButton)

        self.WAlignButton = QToolButton(self.MainArea)
        self.WAlignButton.setObjectName(u"WAlignButton")
        icon5 = QIcon()
        icon5.addFile(u"../WAlignButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.WAlignButton.setIcon(icon5)

        self.horizontalLayout.addWidget(self.WAlignButton)


        self.RandomBullshitLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ChangeText = QToolButton(self.MainArea)
        self.ChangeText.setObjectName(u"ChangeText")

        self.horizontalLayout_2.addWidget(self.ChangeText)

        self.ChangeBack = QToolButton(self.MainArea)
        self.ChangeBack.setObjectName(u"ChangeBack")

        self.horizontalLayout_2.addWidget(self.ChangeBack)

        self.ChangeMargin = QToolButton(self.MainArea)
        self.ChangeMargin.setObjectName(u"ChangeMargin")

        self.horizontalLayout_2.addWidget(self.ChangeMargin)

        self.LineSpace = QToolButton(self.MainArea)
        self.LineSpace.setObjectName(u"LineSpace")

        self.horizontalLayout_2.addWidget(self.LineSpace)


        self.RandomBullshitLayout.addLayout(self.horizontalLayout_2)


        self.ToolPanel.addLayout(self.RandomBullshitLayout, 0, 3, 1, 1)

        self.FontLayout = QHBoxLayout()
        self.FontLayout.setObjectName(u"FontLayout")
        self.FontBox = QFontComboBox(self.MainArea)
        self.FontBox.setObjectName(u"FontBox")
        self.FontBox.setWritingSystem(QFontDatabase.WritingSystem.Latin)
        self.FontBox.setFontFilters(QFontComboBox.FontFilter.ScalableFonts)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        self.FontBox.setCurrentFont(font)

        self.FontLayout.addWidget(self.FontBox)

        self.FontSize = QSpinBox(self.MainArea)
        self.FontSize.setObjectName(u"FontSize")
        self.FontSize.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.FontSize.setMinimum(1)
        self.FontSize.setMaximum(128)
        self.FontSize.setValue(12)

        self.FontLayout.addWidget(self.FontSize)


        self.ToolPanel.addLayout(self.FontLayout, 0, 0, 1, 1)

        self.TextFormatLayout = QHBoxLayout()
        self.TextFormatLayout.setSpacing(10)
        self.TextFormatLayout.setObjectName(u"TextFormatLayout")
        self.TextFormatLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.BoldStyleButton = QPushButton(self.MainArea)
        self.BoldStyleButton.setObjectName(u"BoldStyleButton")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatTextBold))
        self.BoldStyleButton.setIcon(icon6)

        self.TextFormatLayout.addWidget(self.BoldStyleButton)

        self.ItalicStyleButton = QPushButton(self.MainArea)
        self.ItalicStyleButton.setObjectName(u"ItalicStyleButton")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatTextItalic))
        self.ItalicStyleButton.setIcon(icon7)

        self.TextFormatLayout.addWidget(self.ItalicStyleButton)

        self.UnderlineStyleButton = QPushButton(self.MainArea)
        self.UnderlineStyleButton.setObjectName(u"UnderlineStyleButton")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatTextUnderline))
        self.UnderlineStyleButton.setIcon(icon8)

        self.TextFormatLayout.addWidget(self.UnderlineStyleButton)

        self.clearButton = QPushButton(self.MainArea)
        self.clearButton.setObjectName(u"clearButton")
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.clearButton.setIcon(icon9)

        self.TextFormatLayout.addWidget(self.clearButton)


        self.ToolPanel.addLayout(self.TextFormatLayout, 0, 9, 1, 1)


        self.gridLayout.addLayout(self.ToolPanel, 0, 0, 1, 1)

        self.DocumentArea = QScrollArea(self.MainArea)
        self.DocumentArea.setObjectName(u"DocumentArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DocumentArea.sizePolicy().hasHeightForWidth())
        self.DocumentArea.setSizePolicy(sizePolicy1)
        self.DocumentArea.setFrameShape(QFrame.Shape.NoFrame)
        self.DocumentArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.DocumentArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.DocumentArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.DocumentArea.setWidgetResizable(True)
        self.DocumentArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DocumentContent = QWidget()
        self.DocumentContent.setObjectName(u"DocumentContent")
        self.DocumentContent.setGeometry(QRect(0, 0, 984, 1153))
        sizePolicy1.setHeightForWidth(self.DocumentContent.sizePolicy().hasHeightForWidth())
        self.DocumentContent.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.DocumentContent)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textEdit = CustomTextEdit(self.DocumentContent)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(802, 1131))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"border: 1px solid")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)
        self.textEdit.setLineWrapColumnOrWidth(800)

        self.gridLayout_2.addWidget(self.textEdit, 2, 0, 1, 1)

        self.DocumentArea.setWidget(self.DocumentContent)

        self.gridLayout.addWidget(self.DocumentArea, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.MainArea)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1021, 26))
        self.menubar.setDefaultUp(False)
        self.menuTest = QMenu(self.menubar)
        self.menuTest.setObjectName(u"menuTest")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuTest.addAction(self.createDocAction)
        self.menuTest.addAction(self.saveDocAction)
        self.menuTest.addAction(self.openDocAction)
        self.menu.addAction(self.imageAction)
        self.menu.addAction(self.linkAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FEFU \u0421\u043b\u043e\u0432\u043e 2025", None))
        self.createDocAction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0424\u0430\u0439\u043b", None))
        self.imageAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.linkAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0421\u0441\u044b\u043b\u043a\u0443", None))
        self.saveDocAction.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.openDocAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0424\u0430\u0439\u043b", None))
        self.LinkButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ImageButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.LAlignButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CAlignButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.RAlignButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.WAlignButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ChangeText.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.ChangeBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.ChangeMargin.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
        self.LineSpace.setText(QCoreApplication.translate("MainWindow", u"LineSpace", None))
        self.BoldStyleButton.setText("")
        self.ItalicStyleButton.setText("")
        self.UnderlineStyleButton.setText("")
        self.clearButton.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Times New Roman'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430", None))
    # retranslateUi

