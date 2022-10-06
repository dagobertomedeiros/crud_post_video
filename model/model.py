

class ModelPostVideo:

    def __init__(self) -> None:
        pass

    def validate_login(self, login: str, passw: str):
        """
        Valida se login e senha estão corretos.
        """
        if login == "Chico" and passw == "1234":
            return True

    def list_videos(self):
        video_1 = {"name": "Mateus Buente",
                   "description": "Comédia baiana de stand up",
                   "local": "/home/dagoberto/Vídeos/MATHEUS.3gp"}
        return video_1