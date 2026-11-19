import unittest

from saudacao import despedida


class TestDespedida(unittest.TestCase):
    def test_nome(self):
        self.assertEqual(despedida("Ana"), "Adeus, Ana!")

    def test_nome_vazio(self):
        self.assertEqual(despedida(""), "Adeus!")

    def test_nome_so_espacos(self):
        self.assertEqual(despedida("   "), "Adeus!")

    def test_nome_com_espacos_a_volta(self):
        self.assertEqual(despedida(" Ana "), "Adeus, Ana!")

    def test_nome_none(self):
        self.assertEqual(despedida(None), "Adeus, None!")

    def test_nome_nao_string(self):
        self.assertEqual(despedida(42), "Adeus, 42!")

    def test_tabs_e_quebras_de_linha(self):
        self.assertEqual(despedida("\tAna\n"), "Adeus, Ana!")

    def test_espacos_interiores_mantem_se(self):
        self.assertEqual(despedida("Ana Maria"), "Adeus, Ana Maria!")

    def test_so_tabs_e_quebras(self):
        self.assertEqual(despedida("\t\n "), "Adeus!")


if __name__ == "__main__":
    unittest.main()
