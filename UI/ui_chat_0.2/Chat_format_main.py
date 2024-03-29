﻿import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import Chat_format
import otrmanager


form_class = uic.loadUiType("Chat_format.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(MyWindow,self).__init__() # python 버전에 따라 여기 고칠 필요 있음
        self.setupUi(self)
        self.connect(self.sendButton, SIGNAL("clicked()"), self.btn_clicked)

    def btn_clicked(self):
        text = self.chatInput.text()
        id= "two@arewesecureyet.org"
        otrmanager.OTRManager.Instance().SendMessage(id,text)
        self.chatLog.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
