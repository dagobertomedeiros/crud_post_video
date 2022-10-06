#from curses import window
from PyQt5.QtWidgets import QApplication, QMessageBox
from views.login import LoginView
from views.videos import VideosView
from model.model import ModelPostVideo
from utils.utils import Utils

class AppPostVideo:
    """Classe de controle, responsável por iniciar a app e 
       fazer a comunicação entre o model e as views."""

    def __init__(self) -> None:
        self.app = QApplication([])
        self.login = LoginView()
        self.video = VideosView()
        self.model = ModelPostVideo()
        self.utils = Utils()
        self.login.pb_yes.clicked.connect(self.validate_login)
        self.login.pb_no.clicked.connect(self.close_login)

        
    def run(self):
        self.login.screem_login()
        self.app.exec_()

    def validate_login(self):
        login = self.login.le_name.text()
        passw = self.login.le_password.text()
        if self.model.validate_login(login, passw):
            self.close_login()
            self.video.screen_player()
        else:
            self.utils.show_dialog('Login', 'Login ou senha incorreto, verifique, por favor!', QMessageBox.Critical)

    def close_login(self):
        self.login.window.close()

    

if __name__ == "__main__":
    window = AppPostVideo()
    window.run()   

#app = QApplication([])
#window = AppPostVideo()
#app.exec_()
