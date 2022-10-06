from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QDir, Qt, QUrl, QFile
from views.login import LoginView
from views.videos import VideosView
from model.model import ModelPostVideo
from utils.utils import Utils
import os.path

class AppPostVideo:
    """Classe de controle, responsável por fazer a
       comunicação entre o model e as views."""

    def __init__(self) -> None:
        self.app = QApplication([])
        self.login = LoginView()
        self.video = VideosView()
        self.model = ModelPostVideo()
        self.utils = Utils()
        self.login.pb_yes.clicked.connect(self.validate_login)
        self.login.pb_no.clicked.connect(self.close_login)
        self.video.pb_play.setEnabled(False)
        self.video.pb_play.clicked.connect(self.play_video)
        self.video.pb_add.clicked.connect(self.get_videos)
        self.video.slide.sliderMoved.connect(self.position_slide)
        self.video.player.positionChanged.connect(self.position_change)
        self.video.player.durationChanged.connect(self.duration_change)

    def run(self):
        """Inicia app pela tela de login."""
        self.login.screem_login()
        self.app.exec_()

    def validate_login(self):
        """Invoca o model para validar o login."""
        login = self.login.le_name.text()
        passw = self.login.le_password.text()
        if self.model.validate_login(login, passw):
            self.close_login()
            self.video.screen_player()
        else:
            self.utils.show_dialog('Login', 'Login ou senha incorreto, verifique, por favor!',
                                   QMessageBox.Critical)

    def close_login(self):
        """Fecha a janela de login."""
        self.login.window.close()

    def get_videos(self):
        """Recupera os videos para execucao no player."""
        video = self.model.list_videos()
        if video:
            file = os.path.abspath(video['local'])
            print('local file -> ', file, 'type -> ', type(file))
            self.video.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
            self.video.lb_name_video.setText(video['name'])
            self.video.lb_description_video.setText(video['description'])
            self.video.pb_play.setEnabled(True)

    def play_video(self):
        """Valida o status do player permitindo tocar e pausar o video."""
        if self.video.player.state() == QMediaPlayer.PlayingState:
            self.video.player.pause()
        else:
            self.video.player.play()

    def position_slide(self, position):
        """Define a posicao do video no player."""
        self.video.player.setPosition(position)

    def position_change(self, position):
        """Atualiza as mudaças de posicao do cursos da barra de slide."""
        self.video.slide.setValue(position)

    def duration_change(self, duration):
        """Define a duração do video para a barra de slide."""
        self.video.slide.setRange(0, duration)
if __name__ == "__main__":
    window = AppPostVideo()
    window.run()
