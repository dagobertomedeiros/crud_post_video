from PyQt5.QtWidgets import QMessageBox

class Utils:
    """Classe define um conjunto de funções, estilos e recursos que podem
       ser utilizados a qualquer momento."""

    def show_dialog(self, title, message, information):
        msgBox = QMessageBox()
        msgBox.setIcon(information)  # Question, Warning, Critical QMessageBox.Information
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.buttonClicked.connect(self.on_click)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            msgBox.close()

    def on_click(self):
        pass
