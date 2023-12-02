import unittest
from unittest.mock import Mock
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from RelatorioPDF import RelatorioPDF

class TestRelatorioPDF(unittest.TestCase):

    def setUp(self):
        # Configurações iniciais que podem ser usadas em todos os testes
        self.mock_canvas = Mock(spec=canvas.Canvas)

    def test_gerar_relatorio(self):
        # Configuração específica para o teste
        relatorio = RelatorioPDF(
            salario_base=1000.0,
            salario_bruto=1200.0,
            salario_base_de_calculo=900.0,
            anos_vigencia=[2020, 2021],
            salario_liquido=800.0,
            irrf_recolhido=50.0,
            aliquota=0.05,
            nome_contribuinte="João",
            cpf_contribuinte="123.456.789-00"
        )

        # Execução do método a ser testado
        relatorio.gerarrelatorio(self.mock_canvas)

        # Verificação de chamadas ao canvas
        self.mock_canvas.setFillColor.assert_called()
        self.mock_canvas.setFont.assert_called_with("Helvetica", 13)
        self.mock_canvas.drawString.assert_called_with(15, 300, "Bem vindo contribuinte João.")

if __name__ == '__main__':
    unittest.main()
