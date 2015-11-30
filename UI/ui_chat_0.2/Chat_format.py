# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chat_format.ui'
#
# Created: Mon Nov 30 14:45:40 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(424, 522)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/DE_images/lock_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(:/DE_images/blue_image.jpg)"))
        self.chatInput = QtGui.QLineEdit(Dialog)
        self.chatInput.setGeometry(QtCore.QRect(10, 380, 301, 91))
        self.chatInput.setStyleSheet(_fromUtf8("background-image: url(:/DE_images/transparent16x16.png)"))
        self.chatInput.setObjectName(_fromUtf8("chatInput"))
        self.sendButton = QtGui.QPushButton(Dialog)
        self.sendButton.setGeometry(QtCore.QRect(320, 380, 91, 91))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(340, 10, 71, 22))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(197, 245, 253)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.toolButton_4 = QtGui.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(20, 480, 36, 36))
        self.toolButton_4.setMinimumSize(QtCore.QSize(32, 32))
        self.toolButton_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_4.setAutoFillBackground(False)
        self.toolButton_4.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/DE_images/file 32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_5 = QtGui.QToolButton(Dialog)
        self.toolButton_5.setGeometry(QtCore.QRect(100, 480, 36, 36))
        self.toolButton_5.setMinimumSize(QtCore.QSize(32, 32))
        self.toolButton_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_5.setAutoFillBackground(False)
        self.toolButton_5.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/DE_images/search_magifier 32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon2)
        self.toolButton_5.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.toolButton_6 = QtGui.QToolButton(Dialog)
        self.toolButton_6.setGeometry(QtCore.QRect(180, 480, 36, 36))
        self.toolButton_6.setMinimumSize(QtCore.QSize(32, 32))
        self.toolButton_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_6.setAutoFillBackground(False)
        self.toolButton_6.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/DE_images/phone_call 32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon3)
        self.toolButton_6.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.toolButton_7 = QtGui.QToolButton(Dialog)
        self.toolButton_7.setGeometry(QtCore.QRect(260, 480, 36, 36))
        self.toolButton_7.setMinimumSize(QtCore.QSize(32, 32))
        self.toolButton_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolButton_7.setAutoFillBackground(False)
        self.toolButton_7.setStyleSheet(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/DE_images/config2_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon4)
        self.toolButton_7.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 401, 331))
        self.scrollArea.setStyleSheet(_fromUtf8("background-image:url(:/DE_images/transparent16x16.png)"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 329))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.chatLog = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.chatLog.setGeometry(QtCore.QRect(0, 10, 361, 41))
        self.chatLog.setStyleSheet(_fromUtf8("background-image:url(:/DE_images/transparent16x16.png)"))
        self.chatLog.setObjectName(_fromUtf8("chatLog"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalSlider = QtGui.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(320, 490, 91, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SecureChat by Li_Big_A", None))
        self.sendButton.setText(_translate("Dialog", "전송", None))
        self.comboBox.setItemText(0, _translate("Dialog", "메뉴", None))
        self.comboBox.setItemText(1, _translate("Dialog", "대화 검색", None))
        self.comboBox.setItemText(2, _translate("Dialog", "대화 캡쳐", None))
        self.comboBox.setItemText(3, _translate("Dialog", "파일 전송", None))
        self.comboBox.setItemText(4, _translate("Dialog", "채팅방 설정", None))
        self.comboBox.setItemText(5, _translate("Dialog", "채팅방 나가기", None))
        self.comboBox.setItemText(6, _translate("Dialog", "닫기", None))
        self.toolButton_4.setAccessibleName(_translate("Dialog", "\\", None))
        self.toolButton_5.setAccessibleName(_translate("Dialog", "\\", None))
        self.toolButton_6.setAccessibleName(_translate("Dialog", "\\", None))
        self.toolButton_7.setAccessibleName(_translate("Dialog", "\\", None))
        self.chatLog.setText(_translate("Dialog", "chatLog", None))

import DE_images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

