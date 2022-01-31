import unittest

from atividades import comer, dormir, eh_engracado


class AtividadeTeste(unittest.TestCase):
    def test_comer_saudavel(self):
        """testando o retorno com comida saudavel"""
        self.assertEqual(comer("pão", True), "Estou comendo pão porque quero manter a forma.")

    def test_comer_gostosa(self):
        """testando o retorno com comida gostosa"""
        self.assertEqual(comer("pizza", False), "Estou comendo pizza porque a gente só vive uma vez.")

    def test_dormir_pouco(self):
        """testando o retorno domindo pouco"""
        self.assertEqual(dormir(4), "Continuo cansado após dormir por 4 horas. :(")

    def test_dormir_muito(self):
        """testando o retorno domindo muito"""
        self.assertEqual(dormir(10), "Ptz! Dormi muito! Estou atrasado para o trabalho!")

    def test_eh_engracado(self):
        """Testando as pessoas engraçadas"""
        # self.assertEqual(eh_engracado("Vanessa"), False)
        self.assertFalse(eh_engracado("Vanessa"), "Vanessa é bonita!")
        self.assertTrue(eh_engracado("Jin"), "Jin deveria ser engraçado!")


if __name__ == '__main__':
    unittest.main()

