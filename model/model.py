"""Model"""

class ModelPostVideo:
    """Classe que executas validacoes, acessos ao banco e outros."""

    def __init__(self) -> None:
        pass

    def validate_login(self, login: str, passw: str) -> bool:
        """
        Valida se login e senha estão corretos.
        """
        if login == "Chico" and passw == "1234":
            return True
        return None

    def list_videos(self) -> dict[str, str]:
        """
        Retorna as videos disponiveis.
        """
        video_1 = {"name": "Mateus Buente",
                   "description": "Comédia baiana de stand up",
                   "local": "files/MATHEUS.3gp"}
        return video_1
