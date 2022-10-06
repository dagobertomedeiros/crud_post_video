import unittest
from model.model import ModelPostVideo

class TestLogin(unittest.TestCase):
    """Implementa teste automatizado de login."""

    def test_login(self):
        """Valida se funcao de login."""
        
        self.assertTrue(ModelPostVideo.validate_login('Chico', '1234'))

if __name__ == '__main__':
    test = TestLogin()
    test.test_login()