

class ModelPostVideo:

    def __init__(self) -> None:
        pass

    def validate_login(self, login: str, passw: str):
        """
        Valida se login e senha estão corretos.
        """
        if login == "Chico" and passw == "1234":
            return True