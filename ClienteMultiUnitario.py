import pandas as pd

from Grafico import Grafico
from LogicaCalculadora import LogicaCalculadora
from RelatorioPDF import RelatorioPDF

class ClienteMultiUnitario:

    def __init__(self):

       # Carrega os dados do Excel para o DataFrame
        self.entradas_de_multiplas_pessoas = pd.read_excel('entradas_de_multiplas_pessoas.xlsx')

        # Correção: substituição de 'entradas_em_massa' por 'entradas_de_multiplas_pessoas'
        self.n_entradas = len(self.entradas_de_multiplas_pessoas.index)

        self.salario_base_list             =          list(range(self.n_entradas))
        self.bonus_tempo_list              =          list(range(self.n_entradas))
        self.bonus_formacao_list           =          list(range(self.n_entradas))
        self.bonus_periculosidade_list     =          list(range(self.n_entradas))
        self.adicoes                       =          list(range(self.n_entradas))
        self.salario_bruto_list            =          list(range(self.n_entradas))

        self.mesinicio_list =                    list(range(self.n_entradas))
        self.anoinicio_list =                    list(range(self.n_entradas))
        self.mesfim_list =                       list(range(self.n_entradas))
        self.anofim_list =                       list(range(self.n_entradas))

        self.anos_vigencia_aux_list =            list(range(self.n_entradas))

        self.numero_dependentes_list      = list(range(self.n_entradas))
        self.pensao_alimenticia_list      = list(range(self.n_entradas))
        self.outros_descontos_list        = list(range(self.n_entradas))
        self.total_deducoes               = list(range(self.n_entradas))
        self.salario_base_de_calculo_list = list(range(self.n_entradas))

        self.salario_liquido_list      = list(range(self.n_entradas))
        self.irrf_recolhido_list       = list(range(self.n_entradas))
        self.anos_vigencia_list        = list(range(self.n_entradas))
        self.aliquota_list             = list(range(self.n_entradas))

        self.nome_contribuinte_list =                      list(range(self.n_entradas))
        self.cpf_contribuinte_list  =                      list(range(self.n_entradas))
        self.tipooferta_list   =                      list(range(self.n_entradas))

        self.logicacalculadora = None

        self.salario_liquido_list_grafico         = [[0 for i in range(self.anos_vigencia_aux_list)] for j in range(self.n_entradas)]
        self.irrf_recolhido_list_grafico          = [[0 for i in range(self.anos_vigencia_aux_list)] for j in range(self.n_entradas)]
        self.salario_base_list_grafico            = [[0 for i in range(self.anos_vigencia_aux_list)] for j in range(self.n_entradas)]
        self.adicoes_grafico                      = [[0 for i in range(self.anos_vigencia_aux_list)] for j in range(self.n_entradas)]
        self.salario_base_de_calculo_list_grafico = [[0 for i in range(self.anos_vigencia_aux_list)] for j in range(self.n_entradas)]
        self.total_deducoes_grafico               = [[0 for i in range(self.anos_vigencia_aux_list)] for j in range(self.n_entradas)]

    def prencher_variaveis_multiplas(self):

        for i in range(0, self.n_entradas, 1):

            self.salario_base_list[i]             = self.entradas_de_multiplas_pessoas.iloc[i, 0]
            self.bonus_tempo_list[i]              = self.entradas_de_multiplas_pessoas.iloc[i, 1]
            self.bonus_formacao_list[i]           = self.entradas_de_multiplas_pessoas.iloc[i, 2]
            self.bonus_periculosidade_list[i]     = self.entradas_de_multiplas_pessoas.iloc[i, 3]            

            self.mesinicio_list[i] =           self.entradas_de_multiplas_pessoas.iloc[i, 4]
            self.anoinicio_list[i] =           self.entradas_de_multiplas_pessoas.iloc[i, 5]
            self.mesfim_list[i] =              self.entradas_de_multiplas_pessoas.iloc[i, 6]
            self.anofim_list[i] =              self.entradas_de_multiplas_pessoas.iloc[i, 7]
            self.anos_vigencia_aux_list[i] =      self.anofim_list[i] - self.anoinicio_list[i] + 1

            self.numero_dependentes_list[i]      =  self.entradas_de_multiplas_pessoas.iloc[i, 8]
            self.pensao_alimenticia_list[i]      =  self.entradas_de_multiplas_pessoas.iloc[i, 9]
            self.outros_descontos_list[i]        =  self.entradas_de_multiplas_pessoas.iloc[i, 10]

            self.nome_contribuinte_list[i]    =             self.entradas_de_multiplas_pessoas.iloc[i, 11]
            self.cpf_contribuinte_list[i]    =              self.entradas_de_multiplas_pessoas.iloc[i, 12]
            self.tipooferta_list[i] =                  self.entradas_de_multiplas_pessoas.iloc[i, 13]


    def criar_graficos_e_relatorios(self):

        for j in range(0, self.n_entradas, 1):

            logicacalculadoramultipla = LogicaCalculadora(self.salario_base_list[j],self.bonus_tempo_list[j],self.bonus_formacao_list[j],self.bonus_periculosidade_list[j],
                            self.mesinicio_list[j],self.anoinicio_list[j],self.mesfim_list[j],self.anofim_list[j],
                            self.numero_dependentes_list[j],self.pensao_alimenticia_list[j],self.outros_descontos_list[j],self.tipooferta_list[j])

            logicacalculadoramultipla.calculo_bonus_e_salario_bruto()
            logicacalculadoramultipla.calculo_deducoes_e_salario_base()
            logicacalculadoramultipla.calculo_irrf_recolhido_salario_liquido_aliquota()
            logicacalculadoramultipla.definir_anos_vigencia()

            if (self.tipooferta_list[j] == 1):

                self.salario_liquido_list_grafico[j][0], self.irrf_recolhido_list_grafico[j][0], self.anos_vigencia_list[j],
                self.salario_base_list_grafico[j][0], self.adicoes_grafico[j][0],
                self.salario_base_de_calculo_list_grafico[j][0], self.total_deducoes_grafico[j][0] = logicacalculadoramultipla.enviardadosparagrafico()

                self.salario_liquido_list_grafico[j], self.irrf_recolhido_list_grafico[j],
                self.salario_base_list_grafico[j], self.adicoes_grafico[j],
                self.salario_base_de_calculo_list_grafico[j], self.total_deducoes_grafico[j] = logicacalculadoramultipla.preparar_graficos(self.salario_liquido_list_grafico[j][0], self.irrf_recolhido_list_grafico[j][0], self.salario_base_list_grafico[j][0], self.adicoes_grafico[j][0], self.salario_base_de_calculo_list_grafico[j][0], self.total_deducoes_grafico[j][0])

                grafico = Grafico(self.salario_liquido_list_grafico[j], self.irrf_recolhido_list_grafico[j], self.anos_vigencia_list[j], j,
                                  self.salario_base_list_grafico[j], self.adicoes_grafico[j],
                                  self.salario_base_de_calculo_list_grafico[j], self.total_deducoes_grafico[j],
                                  self.nome_contribuinte_list[j])

                grafico.criargrafico1()
                grafico.criargrafico2()
                grafico.criargrafico3()

            if (self.tipooferta_list[j] == 2):

                self.salario_base_list[j], self.salario_bruto_list[j], self.salario_base_de_calculo_list[j],
                self.anos_vigencia_list[j],
                self.salario_liquido_list[j], self.irrf_recolhido_list[j], self.aliquota_list[j] = logicacalculadoramultipla.enviardadospararelatorio()

                self.salario_base_list[j], self.salario_bruto_list[j],
                self.salario_base_de_calculo_list[j], self.salario_liquido_list[j],
                self.irrf_recolhido_list[j] = logicacalculadoramultipla.preparar_relatorio(self.salario_base_list[j], self.salario_bruto_list[j], self.salario_base_de_calculo_list[j], self.salario_liquido_list[j], self.irrf_recolhido_list[j])

                relatoriopdf = RelatorioPDF(self.salario_base_list[j], self.salario_bruto_list[j], self.salario_base_de_calculo_list[j],
                self.anos_vigencia_list[j],
                self.salario_liquido_list[j], self.irrf_recolhido_list[j], self.aliquota_list[j],
                self.nome_contribuinte_list[j], self.cpf_contribuinte_list[j])

                relatoriopdf.gerarrelatorio()
