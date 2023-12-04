import unittest
from ClienteMultiUnitario import ClienteMultiUnitario
import os

class TestCriacaoGraficos(unittest.TestCase):

    def test_criacao_graficos(self):
        # Inicialização e preparação dos dados
        cliente = ClienteMultiUnitario()
        cliente.prencher_variaveis_multiplas()
        
        # Realizar ação - criar gráficos
        cliente.criar_graficos_e_relatorios(tipo_oferta=1)

        # Verificar se os gráficos foram criados
        self.assertTrue(os.path.exists('grafico_contribuinte_x.png')) # Substitua pelo nome correto do arquivo

        # Limpeza - remover arquivos gerados
        os.remove('grafico_contribuinte_x.png')

class TestCriacaoRelatorios(unittest.TestCase):

    def test_criacao_relatorios(self):
        cliente = ClienteMultiUnitario()
        cliente.prencher_variaveis_multiplas()
        
        cliente.criar_graficos_e_relatorios(tipo_oferta=2)

        self.assertTrue(os.path.exists('relatorio_contribuinte_x.pdf'))
        os.remove('relatorio_contribuinte_x.pdf')

class TestPrecisaoCalculos(unittest.TestCase):

    def test_precisao_calculos(self):
        cliente = ClienteMultiUnitario()
        cliente.prencher_variaveis_multiplas()

        # Substitua os valores esperados com base nos cálculos reais
        valor_esperado = {'salario_liquido': 3000, 'irrf_recolhido': 500}
        valores_calculados = cliente.logicacalculadora.calcular()

        self.assertEqual(valores_calculados, valor_esperado)

class TestConsistenciaDados(unittest.TestCase):

    def test_consistencia_dados(self):
        cliente = ClienteMultiUnitario()
        cliente.prencher_variaveis_multiplas()

        cliente.criar_graficos_e_relatorios(tipo_oferta=1)
        cliente.criar_graficos_e_relatorios(tipo_oferta=2)

        # Aqui, você compararia os dados dos gráficos com os dados dos relatórios
        # Isso pode ser feito lendo os arquivos gerados e comparando os valores

        # Lembre-se de limpar os arquivos gerados após o teste
        os.remove('grafico_contribuinte_x.png')
        os.remove('relatorio_contribuinte_x.pdf')
      
class TestIntegracaoMultiplasEntradas(unittest.TestCase):

    def test_multiplas_entradas(self):
        cliente = ClienteMultiUnitario()
        cliente.prencher_variaveis_multiplas()

        for i in range(cliente.n_entradas):
            # Substitua as chamadas de método conforme necessário
            cliente.criar_graficos_e_relatorios(tipo_oferta=cliente.tipooferta_list[i])

            # Verifique se os arquivos correspondentes a cada entrada foram criados
            self.assertTrue(os.path.exists(f'grafico_contribuinte_{i}.png'))
            self.assertTrue(os.path.exists(f'relatorio_contribuinte_{i}.pdf'))

            # Limpeza
            os.remove(f'grafico_contribuinte_{i}.png')
            os.remove(f'relatorio_contribuinte_{i}.pdf')
