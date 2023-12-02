import unittest
from unittest.mock import patch
import numpy as np
from Grafico import Grafico

class TestGrafico(unittest.TestCase):

    def setUp(self):
        self.grafico = Grafico(
            salario_liquido=[1000, 1200, 1500],
            irrf_recolhido=[50, 60, 75],
            anos_vigencia=[2021, 2022, 2023],
            numero_de_graficos=1,
            salario_base=[800, 1000, 1200],
            aditivos=[50, 20, 30],
            salario_base_de_calculo=[750, 900, 1100],
            deducoes=[20, 30, 40],
            nome_contribuinte="Teste"
        )

    def test_criar_grafico1(self):
        with patch("matplotlib.pyplot.show") as mock_show, patch("matplotlib.pyplot.savefig") as mock_savefig:
            self.grafico.criargrafico1()
        mock_show.assert_called_once()
        mock_savefig.assert_called_once_with('Grafico 1 do contribuinte Teste.png', format='png')

    def test_criar_grafico2(self):
        with patch("matplotlib.pyplot.show") as mock_show, patch("matplotlib.pyplot.savefig") as mock_savefig:
            self.grafico.criargrafico2()
        mock_show.assert_called_once()
        mock_savefig.assert_called_once_with('Grafico 2 do contribuinte Teste.png', format='png')

    def test_criar_grafico3(self):
        with patch("matplotlib.pyplot.show") as mock_show, patch("matplotlib.pyplot.savefig") as mock_savefig:
            self.grafico.criargrafico3()
        mock_show.assert_called_once()
        mock_savefig.assert_called_once_with('grafico do contribuinte Teste.png', format='png')

if __name__ == '__main__':
    unittest.main()
