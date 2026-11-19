import unittest

from saudacao import saudacao


class TestSaudacao(unittest.TestCase):
    def test_nome(self):
        self.assertEqual(saudacao("Ana"), "Olá, Ana!")

    def test_nome_vazio(self):
        self.assertEqual(saudacao(""), "Olá!")

    def test_nome_so_espacos(self):
        self.assertEqual(saudacao("   "), "Olá!")

    def test_nome_com_espacos_a_volta(self):
        self.assertEqual(saudacao(" Ana "), "Olá, Ana!")

    def test_nome_none_mantem_comportamento_antigo(self):
        self.assertEqual(saudacao(None), "Olá, None!")


if __name__ == "__main__":
    unittest.main()
