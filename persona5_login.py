# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'persona5_login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_loginWidget(object):
    def setupUi(self, loginWidget):
        if not loginWidget.objectName():
            loginWidget.setObjectName(u"loginWidget")
        loginWidget.resize(812, 610)
        loginWidget.setMinimumSize(QSize(812, 610))
        loginWidget.setMaximumSize(QSize(812, 610))
        font = QFont()
        font.setFamilies([u"p5hatty"])
        font.setPointSize(28)
        loginWidget.setFont(font)
        loginWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        loginWidget.setAutoFillBackground(False)
        loginWidget.setStyleSheet(u"background-color: white;")
        self.frame = QFrame(loginWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 791, 591))
        self.frame.setStyleSheet(u"QFrame {background-color: black; border: none; border-radius: 20px;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(180, 90, 441, 241))
        font1 = QFont()
        font1.setFamilies([u"p5hatty"])
        font1.setPointSize(13)
        self.image.setFont(font1)
        self.image.setPixmap(QPixmap(u"Persona 5 Project\images\mask_1.png"))
        self.image.setScaledContents(True)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setMargin(0)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 340, 461, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.password.setFont(font2)
        self.password.setStyleSheet(u"QLineEdit {background-color: grey; border-radius: 15px;}\n"
"QLineEdit:hover:!pressed {background-color: red; border-radius: 15px;}")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setCursorPosition(7)
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.password.setClearButtonEnabled(True)
        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(520, 390, 111, 41))
        font3 = QFont()
        font3.setFamilies([u"p5hatty"])
        font3.setPointSize(30)
        self.loginButton.setFont(font3)
        self.loginButton.setStyleSheet(u"QPushButton {background-color: grey; border: 2px solid grey; border-radius: 15px;}\n"
"QPushButton:hover:!pressed {background-color: red; border: 2px solid black; border-radius: 15px;}")
        self.descriptionBottom = QLabel(self.frame)
        self.descriptionBottom.setObjectName(u"descriptionBottom")
        self.descriptionBottom.setGeometry(QRect(620, 570, 171, 16))
        self.descriptionBottom.setFont(font1)
        self.descriptionBottom.setStyleSheet(u"color:white; background-color: none;")
        self.customTitleBar = QFrame(self.frame)
        self.customTitleBar.setObjectName(u"customTitleBar")
        self.customTitleBar.setGeometry(QRect(10, 10, 771, 31))
        self.customTitleBar.setStyleSheet(u"QFrame {background-color: black;}")
        self.customTitleBar.setFrameShape(QFrame.StyledPanel)
        self.customTitleBar.setFrameShadow(QFrame.Raised)
        self.titleBarLabel = QLabel(self.customTitleBar)
        self.titleBarLabel.setObjectName(u"titleBarLabel")
        self.titleBarLabel.setGeometry(QRect(10, 0, 51, 31))
        font4 = QFont()
        font4.setFamilies([u"p5hatty"])
        font4.setPointSize(18)
        self.titleBarLabel.setFont(font4)
        self.titleBarLabel.setStyleSheet(u"color: white;")
        self.closeButton = QPushButton(self.customTitleBar)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(750, 0, 20, 20))
        font5 = QFont()
        font5.setFamilies([u"p5hatty"])
        font5.setPointSize(1)
        self.closeButton.setFont(font5)
        self.closeButton.setStyleSheet(u"QPushButton {background-color: white; border: none; border-radius: 10px;}\n"
"\n"
"QPushButton:hover:!pressed {background-color: red; border: 5px solid black; border-radius: 250px;}")
        self.closeButton_2 = QPushButton(self.customTitleBar)
        self.closeButton_2.setObjectName(u"closeButton_2")
        self.closeButton_2.setGeometry(QRect(710, 0, 20, 20))
        self.closeButton_2.setFont(font5)
        self.closeButton_2.setStyleSheet(u"QPushButton {background-color: rgb(85, 0, 255); border: none; border-radius: 10px;}\n"
"\n"
"QPushButton:hover:!pressed {background-color: red; border: 5px solid black; border-radius: 250px;}")

        self.retranslateUi(loginWidget)

        QMetaObject.connectSlotsByName(loginWidget)
    # setupUi

    def retranslateUi(self, loginWidget):
        loginWidget.setWindowTitle(QCoreApplication.translate("loginWidget", u"Login", None))
        self.image.setText("")
        self.password.setText(QCoreApplication.translate("loginWidget", u"p5guide", None))
        self.loginButton.setText(QCoreApplication.translate("loginWidget", u"Login", None))
        self.descriptionBottom.setText(QCoreApplication.translate("loginWidget", u"A simple Persona 5 guide //", None))
        self.titleBarLabel.setText(QCoreApplication.translate("loginWidget", u"Login", None))
        self.closeButton.setText("")
        self.closeButton_2.setText("")
    # retranslateUi

