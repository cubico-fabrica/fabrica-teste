import unittest

from iniciais import iniciais


class TestIniciais(unittest.TestCase):
    def test_nome_e_apelido(self):
        self.assertEqual(iniciais("Ana Silva"), "A. S.")

    def test_so_um_nome(self):
        self.assertEqual(iniciais("Ana"), "A.")

    def test_tres_palavras_um_espaco_entre_iniciais(self):
        self.assertEqual(iniciais("Ana Maria Silva"), "A. M. S.")

    def test_espacos_extra_a_volta_e_entre_palavras(self):
        self.assertEqual(iniciais("  Ana   Silva  "), "A. S.")

    def test_espacos_dois_no_inicio_tres_no_meio_um_no_fim(self):
        self.assertEqual(iniciais("  Ana   Silva "), "A. S.")

    def test_tab_entre_palavras(self):
        self.assertEqual(iniciais("Ana\tSilva"), "A. S.")

    def test_minusculas_preservadas(self):
        self.assertEqual(iniciais("ana silva"), "a. s.")

    def test_nome_vazio(self):
        self.assertEqual(iniciais(""), "")

    def test_nome_so_espacos(self):
        self.assertEqual(iniciais("   "), "")

    def test_acentos_preservados(self):
        self.assertEqual(iniciais("Élio Ândrade"), "É. Â.")


if __name__ == "__main__":
    unittest.main()
