import unittest
from RelatorioPDF import RelatorioPDF
import os

class TestRelatorioPDF(unittest.TestCase):

    def test_gerar_relatorio(self):
        # Inicializa a classe
        relatorio = RelatorioPDF(
            salario_base=3000, 
            salario_bruto=3800, 
            salario_base_de_calculo=2500,
            anos_vigencia=['2021', '2022', '2023'],
            salario_liquido=3400, 
            irrf_recolhido=400, 
            aliquota=0.1,
            nome_contribuinte="Teste", 
            cpf_contribuinte="123.456.789-00"
        )

        # Chame o método gerarrelatorio
        relatorio.gerarrelatorio()

        # Verifique se o arquivo PDF foi criado
        nome_arquivo = "Relatório de desconto de Teste.pdf"
        self.assertTrue(os.path.isfile(nome_arquivo))

        # Limpeza: remova o arquivo PDF após o teste
        if os.path.isfile(nome_arquivo):
            os.remove(nome_arquivo)

if __name__ == '__main__':
    unittest.main()

