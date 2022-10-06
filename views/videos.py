from PyQt5.QtWidgets import (QFormLayout, QHBoxLayout, QLineEdit, 
                             QWidget, QPushButton, QApplication,
                             QGridLayout, QVBoxLayout, QLabel,
                             QSlider, QStyle, QMainWindow)
from PyQt5.QtCore import Qt
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer
from utils.utils import Utils
import sys

class VideosView(QMainWindow):
    """Classe que implementa janela e player do video."""

    def __init__(self, parent=None):
        super(VideosView, self).__init__(parent)
        self.utils = Utils()
        self.window = QWidget()
        self.window.setWindowTitle("Player vídeo")
        self.vb_lay = QVBoxLayout()
        self.grid_lay_play = QGridLayout()
        self.grid_lay_crud = QGridLayout()
        self.lb_name_video = QLabel()
        self.lb_name_video.setFixedSize(600, 25)
        self.lb_name_video.setFont(self.utils.format_bold_text())
        self.lb_description_video = QLabel()
        self.lb_description_video.setFixedSize(600, 25)
        self.lb_description_error = QLabel()
        self.wd_video = QVideoWidget()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.slide = QSlider(Qt.Horizontal)
        self.slide.setRange(0, 0)
        self.slide.sliderMoved.connect(self.setPos)
        self.pb_play = QPushButton()
        self.pb_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pb_play.setToolTip('Reproduzir vídeo')
        self.pb_add = QPushButton()
        self.pb_add.setIcon(self.style().standardIcon(QStyle.SP_FileDialogNewFolder))
        self.pb_add.setToolTip('Adicionar vídeo')
        self.pb_remove = QPushButton()
        self.pb_remove.setIcon(self.style().standardIcon(QStyle.SP_TrashIcon))
        self.pb_remove.setToolTip('Remover vídeo')
        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText('Buscar vídeos')
        

    def screen_player(self):
        self.lb_name_video.setText('Nome vídeo')
        self.lb_description_video.setText('Descrição vídeo')
        self.vb_lay.addWidget(self.lb_name_video)
        self.vb_lay.addWidget(self.lb_description_video)
        self.vb_lay.addWidget(self.wd_video)
        self.grid_lay_play.addWidget(self.pb_play, 0, 0)
        self.grid_lay_play.addWidget(self.slide, 0, 1)
        self.vb_lay.addLayout(self.grid_lay_play)
        self.grid_lay_crud.addWidget(self.pb_add, 0, 0)
        self.grid_lay_crud.addWidget(self.pb_remove, 0, 1)
        self.grid_lay_crud.addWidget(self.le_search, 0, 2)
        self.vb_lay.setContentsMargins(0, 0, 0, 0)
        self.vb_lay.addLayout(self.grid_lay_crud)
        #self.vb_lay.setStretch(0, 20)
        #self.vb_lay.setStretch(1, 20)


        #self.pb_yes.setFixedSize(100, 25)
        #self.pb_no.setFixedSize(100, 25)
        #self.form_lay.addRow('Usuário: ', self.le_name)
        #self.form_lay.addRow('Senha: ', self.le_password)
        #self.hb_lay.addWidget(self.pb_yes)
        #self.hb_lay.addWidget(self.pb_no)
        #self.form_lay.addRow(self.hb_lay)
        self.window.setLayout(self.vb_lay)
        self.player.setVideoOutput(self.wd_video)
        #self.form_lay.setFormAlignment(Qt.AlignHCenter)
        #app = QApplication.instance()
        #allScreen = app.primaryScreen()
        #geometry = allScreen.availableGeometry()
        #print(geometry.width())
        self.window.resize(640, 480)

        self.window.show()
        
    def setPos(self, position):
        self.player.setPosition(position)

    def get_password(self):
        pass