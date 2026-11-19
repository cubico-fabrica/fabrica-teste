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

    def test_nome_minusculas_fica_com_maiusculas(self):
        self.assertEqual(saudacao("ana silva"), "Olá, Ana Silva!")

    def test_nome_uma_palavra(self):
        self.assertEqual(saudacao("ana"), "Olá, Ana!")

    def test_nome_ja_capitalizado_fica_igual(self):
        self.assertEqual(saudacao("Ana Silva"), "Olá, Ana Silva!")

    def test_resto_da_palavra_nao_muda(self):
        self.assertEqual(saudacao("ANA SILVA"), "Olá, ANA SILVA!")
        self.assertEqual(saudacao("ana mcDonald"), "Olá, Ana McDonald!")

    def test_letras_acentuadas_no_inicio(self):
        self.assertEqual(saudacao("álvaro éden"), "Olá, Álvaro Éden!")

    def test_particulas_tambem_levam_maiuscula(self):
        self.assertEqual(saudacao("maria da silva"), "Olá, Maria Da Silva!")

    def test_hifen_e_apostrofo_nao_iniciam_palavra(self):
        self.assertEqual(saudacao("ana-maria"), "Olá, Ana-maria!")
        self.assertEqual(saudacao("d'ávila"), "Olá, D'ávila!")

    def test_espacos_nas_pontas_retirados_e_maiusculas(self):
        self.assertEqual(saudacao("  ana silva  "), "Olá, Ana Silva!")

    def test_espacos_entre_palavras_preservados(self):
        self.assertEqual(saudacao("ana  silva"), "Olá, Ana  Silva!")

    def test_palavra_comeca_por_nao_letra(self):
        self.assertEqual(saudacao("3ana"), "Olá, 3ana!")

    def test_valor_nao_str_mantem_comportamento(self):
        self.assertEqual(saudacao(5), "Olá, 5!")


if __name__ == "__main__":
    unittest.main()
