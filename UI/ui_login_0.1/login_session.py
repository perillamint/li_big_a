# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_session.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(553, 710)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("-윤디자인웹돋움"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/DH_images/lock_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 511, 661))
        self.frame.setStyleSheet(_fromUtf8("background-image:url(:/DH_images/blue_image.jpg)"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.input_ID = QtGui.QLineEdit(self.frame)
        self.input_ID.setGeometry(QtCore.QRect(180, 360, 161, 41))
        self.input_ID.setText(_fromUtf8(""))
        self.input_ID.setObjectName(_fromUtf8("input_ID"))
        self.label_ID = QtGui.QLabel(self.frame)
        self.label_ID.setGeometry(QtCore.QRect(50, 360, 121, 41))
        self.label_ID.setStyleSheet(_fromUtf8("QLabel{\n"
"font: italic 12pt \"Comic Sans MS\";\n"
"}\n"
""))
        self.label_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ID.setObjectName(_fromUtf8("label_ID"))
        self.label_password = QtGui.QLabel(self.frame)
        self.label_password.setGeometry(QtCore.QRect(50, 410, 121, 41))
        self.label_password.setStyleSheet(_fromUtf8("QLabel{\n"
"    font: italic 12pt \"Comic Sans MS\";\n"
"}\n"
""))
        self.label_password.setAlignment(QtCore.Qt.AlignCenter)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.input_password = QtGui.QLineEdit(self.frame)
        self.input_password.setEnabled(True)
        self.input_password.setGeometry(QtCore.QRect(180, 410, 161, 41))
        self.input_password.setText(_fromUtf8(""))
        self.input_password.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.input_password.setDragEnabled(False)
        self.input_password.setReadOnly(False)
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.btn_login = QtGui.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(350, 410, 111, 41))
        self.btn_login.setAcceptDrops(False)
        self.btn_login.setAutoFillBackground(False)
        self.btn_login.setStyleSheet(_fromUtf8("font: italic 12pt \"Comic Sans MS\";"))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_register = QtGui.QPushButton(self.frame)
        self.btn_register.setGeometry(QtCore.QRect(340, 490, 121, 41))
        self.btn_register.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_register.setAcceptDrops(False)
        self.btn_register.setAutoFillBackground(False)
        self.btn_register.setStyleSheet(_fromUtf8("font: italic 12pt \"Comic Sans MS\";"))
        self.btn_register.setCheckable(False)
        self.btn_register.setChecked(False)
        self.btn_register.setAutoDefault(False)
        self.btn_register.setDefault(False)
        self.btn_register.setFlat(False)
        self.btn_register.setObjectName(_fromUtf8("btn_register"))
        self.text_register = QtGui.QTextEdit(self.frame)
        self.text_register.setGeometry(QtCore.QRect(60, 490, 261, 41))
        self.text_register.setStyleSheet(_fromUtf8("QTextEdit{\n"
"font: 12pt \"-윤디자인웹돋움\";\n"
"background-image:url(:/DH_images/transparent16x16.png);\n"
"}\n"
""))
        self.text_register.setObjectName(_fromUtf8("text_register"))
        self.timeEdit = QtGui.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(60, 540, 391, 41))
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 1), QtCore.QTime(13, 13, 0)))
        self.timeEdit.setDate(QtCore.QDate(2015, 12, 1))
        self.timeEdit.setTime(QtCore.QTime(13, 13, 0))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 320, 431, 281))
        self.frame_2.setStyleSheet(_fromUtf8("background-image:url(:/DH_images/transparent16x16.png)"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 56, 12))
        self.label.setStyleSheet(_fromUtf8("background-image: url(:/DH_images/transparent16x16.png)"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 56, 12))
        self.label_2.setStyleSheet(_fromUtf8("background-image: url(:/DH_images/transparent16x16.png)"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 71, 81))
        self.label_3.setStyleSheet(_fromUtf8("background-image:url(:/DH_images/finger_print.png)"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(47)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("background-image: url(:/DH_images/transparent16x16.png)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frame_2.raise_()
        self.input_ID.raise_()
        self.label_ID.raise_()
        self.label_password.raise_()
        self.input_password.raise_()
        self.btn_login.raise_()
        self.btn_register.raise_()
        self.text_register.raise_()
        self.timeEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Chat by li_big_a", None))
        self.label_ID.setText(_translate("MainWindow", "ID", None))
        self.label_password.setText(_translate("MainWindow", "PASSWORD", None))
        self.btn_login.setText(_translate("MainWindow", "Login", None))
        self.btn_register.setText(_translate("MainWindow", "Register Now!", None))
        self.text_register.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'-윤디자인웹돋움\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\';\">If you don\'t have an account,</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "Secure Chat", None))

import DH_images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

