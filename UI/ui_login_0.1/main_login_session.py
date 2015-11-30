import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import login

form_class = uic.loadUiType("login_session.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(MyWindow,self).__init__() # python 버전에 따라 여기 고칠 필요 있음
        self.setupUi(self)
        self.connect(self.btn_login, SIGNAL("clicked()"), self.btn_clicked)
        
    def btn_clicked(self):
        ID = self.input_ID.text()
        password = self.input_password.text()

        xmpp = connectClient(ID,password)
        xmpp.register_plugin('xep_0030')
        xmpp.register_plugin('xep_0004')
        xmpp.register_plugin('xep_0060')
        xmpp.register_plugin('xep_0199')
        xmpp.connect()
        xmpp.process()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
