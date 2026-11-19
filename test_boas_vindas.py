import unittest

from saudacao import boas_vindas


class TestBoasVindas(unittest.TestCase):
    def test_nome(self):
        self.assertEqual(boas_vindas("Ana"), "Bem-vinda, Ana!")

    def test_nome_vazio(self):
        self.assertEqual(boas_vindas(""), "Bem-vinda!")

    def test_nome_so_espacos(self):
        self.assertEqual(boas_vindas("   "), "Bem-vinda!")

    def test_nome_com_espacos_a_volta(self):
        self.assertEqual(boas_vindas(" Ana "), "Bem-vinda, Ana!")

    def test_nome_none(self):
        self.assertEqual(boas_vindas(None), "Bem-vinda, None!")

    def test_nome_nao_string(self):
        self.assertEqual(boas_vindas(42), "Bem-vinda, 42!")

    def test_tabs_e_quebras_de_linha(self):
        self.assertEqual(boas_vindas("\tAna\n"), "Bem-vinda, Ana!")

    def test_espacos_interiores_mantem_se(self):
        self.assertEqual(boas_vindas("Ana Maria"), "Bem-vinda, Ana Maria!")

    def test_so_tabs_e_quebras(self):
        self.assertEqual(boas_vindas("\t\n "), "Bem-vinda!")


if __name__ == "__main__":
    unittest.main()
