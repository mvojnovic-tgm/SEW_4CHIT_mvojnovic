# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myGame.ui'
#
# Created: Mon Nov  7 19:03:07 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MyGame(object):
    def setupUi(self, MyGame):
        MyGame.setObjectName("MyGame")
        MyGame.resize(699, 282)
        self.centralwidget = QtGui.QWidget(MyGame)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pb7 = QtGui.QPushButton(self.centralwidget)
        self.pb7.setObjectName("pb7")
        self.gridLayout.addWidget(self.pb7, 0, 8, 1, 1)
        self.pb11 = QtGui.QPushButton(self.centralwidget)
        self.pb11.setObjectName("pb11")
        self.gridLayout.addWidget(self.pb11, 0, 1, 1, 1)
        self.pb9 = QtGui.QPushButton(self.centralwidget)
        self.pb9.setObjectName("pb9")
        self.gridLayout.addWidget(self.pb9, 0, 2, 1, 1)
        self.pb1 = QtGui.QPushButton(self.centralwidget)
        self.pb1.setObjectName("pb1")
        self.gridLayout.addWidget(self.pb1, 1, 6, 1, 1)
        self.pb12 = QtGui.QPushButton(self.centralwidget)
        self.pb12.setObjectName("pb12")
        self.gridLayout.addWidget(self.pb12, 1, 1, 1, 1)
        self.pb14 = QtGui.QPushButton(self.centralwidget)
        self.pb14.setObjectName("pb14")
        self.gridLayout.addWidget(self.pb14, 1, 0, 1, 1)
        self.pb13 = QtGui.QPushButton(self.centralwidget)
        self.pb13.setObjectName("pb13")
        self.gridLayout.addWidget(self.pb13, 1, 2, 1, 1)
        self.pb8 = QtGui.QPushButton(self.centralwidget)
        self.pb8.setObjectName("pb8")
        self.gridLayout.addWidget(self.pb8, 0, 0, 1, 1)
        self.pb10 = QtGui.QPushButton(self.centralwidget)
        self.pb10.setObjectName("pb10")
        self.gridLayout.addWidget(self.pb10, 0, 6, 1, 1)
        self.pb15 = QtGui.QPushButton(self.centralwidget)
        self.pb15.setObjectName("pb15")
        self.gridLayout.addWidget(self.pb15, 2, 2, 1, 1)
        self.pb4 = QtGui.QPushButton(self.centralwidget)
        self.pb4.setObjectName("pb4")
        self.gridLayout.addWidget(self.pb4, 2, 8, 1, 1)
        self.pb2 = QtGui.QPushButton(self.centralwidget)
        self.pb2.setObjectName("pb2")
        self.gridLayout.addWidget(self.pb2, 2, 1, 1, 1)
        self.pb3 = QtGui.QPushButton(self.centralwidget)
        self.pb3.setObjectName("pb3")
        self.gridLayout.addWidget(self.pb3, 2, 0, 1, 1)
        self.pb5 = QtGui.QPushButton(self.centralwidget)
        self.pb5.setObjectName("pb5")
        self.gridLayout.addWidget(self.pb5, 2, 6, 1, 1)
        self.pb6 = QtGui.QPushButton(self.centralwidget)
        self.pb6.setObjectName("pb6")
        self.gridLayout.addWidget(self.pb6, 1, 8, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 5, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout.addWidget(self.pushButton_17)
        self.ende = QtGui.QPushButton(self.centralwidget)
        self.ende.setObjectName("ende")
        self.horizontalLayout.addWidget(self.ende)
        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l2 = QtGui.QLabel(self.centralwidget)
        self.l2.setObjectName("l2")
        self.gridLayout_2.addWidget(self.l2, 5, 2, 1, 1)
        self.spiele = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.spiele.setFont(font)
        self.spiele.setObjectName("spiele")
        self.gridLayout_2.addWidget(self.spiele, 8, 1, 1, 1)
        self.l1 = QtGui.QLabel(self.centralwidget)
        self.l1.setObjectName("l1")
        self.gridLayout_2.addWidget(self.l1, 4, 2, 1, 1)
        self.l4 = QtGui.QLabel(self.centralwidget)
        self.l4.setObjectName("l4")
        self.gridLayout_2.addWidget(self.l4, 7, 2, 1, 1)
        self.offen = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.offen.setFont(font)
        self.offen.setObjectName("offen")
        self.gridLayout_2.addWidget(self.offen, 4, 1, 1, 1)
        self.falsch = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.falsch.setFont(font)
        self.falsch.setObjectName("falsch")
        self.gridLayout_2.addWidget(self.falsch, 6, 1, 1, 1)
        self.gesamt = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.gesamt.setFont(font)
        self.gesamt.setObjectName("gesamt")
        self.gridLayout_2.addWidget(self.gesamt, 7, 1, 1, 1)
        self.korrekt = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.korrekt.setFont(font)
        self.korrekt.setObjectName("korrekt")
        self.gridLayout_2.addWidget(self.korrekt, 5, 1, 1, 1)
        self.l5 = QtGui.QLabel(self.centralwidget)
        self.l5.setObjectName("l5")
        self.gridLayout_2.addWidget(self.l5, 8, 2, 1, 1)
        self.l3 = QtGui.QLabel(self.centralwidget)
        self.l3.setObjectName("l3")
        self.gridLayout_2.addWidget(self.l3, 6, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 5, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 1, 1, 1, 1)
        MyGame.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MyGame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 21))
        self.menubar.setObjectName("menubar")
        MyGame.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MyGame)
        self.statusbar.setObjectName("statusbar")
        MyGame.setStatusBar(self.statusbar)

        self.retranslateUi(MyGame)
        QtCore.QMetaObject.connectSlotsByName(MyGame)

    def retranslateUi(self, MyGame):
        MyGame.setWindowTitle(QtGui.QApplication.translate("MyGame", "MyGame", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MyGame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Druecken sie die Buttons in aufsteigender Richtung!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pb7.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb11.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb9.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb1.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb12.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb14.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb13.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb8.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb10.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb15.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb4.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb2.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb3.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb5.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pb6.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("MyGame", "Neu", None, QtGui.QApplication.UnicodeUTF8))
        self.ende.setText(QtGui.QApplication.translate("MyGame", "Ende", None, QtGui.QApplication.UnicodeUTF8))
        self.l2.setText(QtGui.QApplication.translate("MyGame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.spiele.setText(QtGui.QApplication.translate("MyGame", "Spiele:", None, QtGui.QApplication.UnicodeUTF8))
        self.l1.setText(QtGui.QApplication.translate("MyGame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.l4.setText(QtGui.QApplication.translate("MyGame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.offen.setText(QtGui.QApplication.translate("MyGame", "offen:", None, QtGui.QApplication.UnicodeUTF8))
        self.falsch.setText(QtGui.QApplication.translate("MyGame", "falsch:", None, QtGui.QApplication.UnicodeUTF8))
        self.gesamt.setText(QtGui.QApplication.translate("MyGame", "gesamt:", None, QtGui.QApplication.UnicodeUTF8))
        self.korrekt.setText(QtGui.QApplication.translate("MyGame", "korrekt:", None, QtGui.QApplication.UnicodeUTF8))
        self.l5.setText(QtGui.QApplication.translate("MyGame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.l3.setText(QtGui.QApplication.translate("MyGame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
