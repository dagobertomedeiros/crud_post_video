from PyQt5.QtWidgets import (QFormLayout, QHBoxLayout, QLineEdit, 
                             QWidget, QPushButton, QApplication)
from PyQt5.QtCore import Qt
#import sys
class LoginView:

    def __init__(self, *args, **kargs):
        super(LoginView, self).__init__(*args, **kargs)
        self.window = QWidget()
        self.window.setWindowTitle("Login post vídeo")
        self.form_lay = QFormLayout()
        self.le_name = QLineEdit()
        self.le_password = QLineEdit()
        self.le_password.setEchoMode(QLineEdit.Password)
        self.pb_yes = QPushButton('Confirmar')
        self.pb_no = QPushButton('Cancelar')
        self.hb_lay = QHBoxLayout()
        self.pb_yes.setFixedSize(100, 25)
        self.pb_no.setFixedSize(100, 25)
        self.form_lay.addRow('Usuário: ', self.le_name)
        self.form_lay.addRow('Senha: ', self.le_password)
        self.hb_lay.addWidget(self.pb_yes)
        self.hb_lay.addWidget(self.pb_no)
        self.form_lay.addRow(self.hb_lay)
        self.window.setLayout(self.form_lay)
        self.form_lay.setFormAlignment(Qt.AlignHCenter)
       

    def screem_login(self):
        """
        Carrega a janela de login, defindo suas dimensões.
        """
        self.window.setGeometry(400, 800, 300, 110)
        self.window.show()
        
    