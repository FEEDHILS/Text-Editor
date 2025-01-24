# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_DialogWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(564, 223)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.HeightLabel = QLabel(self.centralwidget)
        self.HeightLabel.setObjectName(u"HeightLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeightLabel.sizePolicy().hasHeightForWidth())
        self.HeightLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.HeightLabel.setFont(font)

        self.gridLayout.addWidget(self.HeightLabel, 2, 0, 1, 1)

        self.WidthLabel = QLabel(self.centralwidget)
        self.WidthLabel.setObjectName(u"WidthLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WidthLabel.sizePolicy().hasHeightForWidth())
        self.WidthLabel.setSizePolicy(sizePolicy1)
        self.WidthLabel.setFont(font)

        self.gridLayout.addWidget(self.WidthLabel, 1, 0, 1, 1)

        self.WidthBox = QSpinBox(self.centralwidget)
        self.WidthBox.setObjectName(u"WidthBox")
        self.WidthBox.setMinimum(1)
        self.WidthBox.setMaximum(3000)

        self.gridLayout.addWidget(self.WidthBox, 1, 1, 1, 1)

        self.HeightBox = QSpinBox(self.centralwidget)
        self.HeightBox.setObjectName(u"HeightBox")
        self.HeightBox.setMinimum(1)
        self.HeightBox.setMaximum(3000)

        self.gridLayout.addWidget(self.HeightBox, 2, 1, 1, 1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HeightLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.WidthLabel.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
    # retranslateUi

