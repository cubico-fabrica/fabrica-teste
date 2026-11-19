import unittest

from saudacao import saudacao


class TestSaudacao(unittest.TestCase):
    def test_nome(self):
        self.assertEqual(saudacao("Ana"), "Olá, Ana!")


if __name__ == "__main__":
    unittest.main()
