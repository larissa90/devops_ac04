from unittest import TestCase
from com.larissa.operacoes import ImprimirLinhas

class Test_ImprimirLinhas(TestCase):
    def setUp(self):
        self.operacoes = ImprimirLinhas()

    def test_linhaSimples(self):
        self.assertEqual(self.operacoes.linhaSimples(5),2, "teste")