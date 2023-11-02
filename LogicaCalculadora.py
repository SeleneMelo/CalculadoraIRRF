import numpy as np
import numpy_financial as npf
import pandas as pd

from copy import deepcopy
from datetime import datetime as dt

#Entradas - Início

#Imposto de Renda retido na fonte = [(Salário bruto - dependentes - INSS) X alíquota] - dedução
#Pesquisar tabela de calculos de INSS e IRRF

class LogicaCalculadora:

    def __init__(self, salario_base, bonus_tempo, bonus_formacao, bonus_periculosidade,
            mes_inicio,ano_inicio,mes_fim,ano_fim,
            numero_dependentes,pensao_alimenticia,outros_descontos,tipooferta):

        self.salario_base                  = salario_base
        self.bonus_tempo                   = bonus_tempo
        self.bonus_formacao                = bonus_formacao
        self.bonus_periculosidade          = bonus_periculosidade

        self.mes_inicio             = mes_inicio
        self.ano_inicio             = ano_inicio
        self.mes_fim                = mes_fim
        self.ano_fim                = ano_fim

        self.numero_dependentes     = numero_dependentes
        self.pensao_alimenticia     = pensao_alimenticia
        self.outros_descontos       = outros_descontos
        self.tipooferta             = tipooferta

        self.salario_base_de_calculo = None
        self.salario_liquido        = None
        self.anos_vigencia            = None
        self.irrf_recolhido = 0


    def formulas_entrada(self):

        self.salario_bruto = self.salario_base + self.bonus_tempo + self.bonus_formacao + self.bonus_periculosidade

        desconto_inss = 0

        if (self.salario_bruto <= 1320.00):
            desconto_inss = self.salario_bruto * 0.075

        elif (1320.01 <= self.salario_bruto <= 2571.29):
            desconto_inss = ((self.salario_bruto - 1320.01) * 0.09) + 99.00

        elif (2571.30 <= self.salario_bruto <= 3856.94):
            desconto_inss = ((self.salario_bruto - 2571.30) * 0.12) + 112.62 + 99.00

        elif (3856.95 <= self.salario_bruto <= 7507.49):
            desconto_inss = ((self.salario_bruto - 3856.95) * 0.14) + 154.28 + 112.62 + 99.00

        else:
            desconto_inss = 876.97

        desconto_dependente = self.numero_dependentes * 189.59

        self.total_deducoes = desconto_inss + desconto_dependente + self.pensao_alimenticia + self.outros_descontos

        self.salario_base_de_calculo = self.salario_bruto - self.total_deducoes

        if (self.salario_base_de_calculo <= 2112.00):
            self.irrf_recolhido = 0

        elif (2112.01 <= self.salario_base_de_calculo <= 2826.65):
            self.irrf_recolhido = ((self.salario_base_de_calculo - 2112.01) * 0.075)

        elif (2826.66 <= self.salario_base_de_calculo <= 3751.05):
            self.irrf_recolhido = ((self.salario_base_de_calculo - 2826.66) * 0.15) + 53.60

        elif (3751.06 <= self.salario_base_de_calculo <= 4664.68):
            self.irrf_recolhido = ((self.salario_base_de_calculo - 3751.06) * 0.225) + 138.66 + 53.60

        elif (self.salario_base_de_calculo > 4664.68):
            self.irrf_recolhido = ((self.salario_base_de_calculo - 4664.68) * 0.275) + 205.56 + 138.66 + 53.60

        self.salario_liquido = self.salario_base_de_calculo - self.irrf_recolhido

        self.aliquota_ = self.irrf_recolhido/self.salario_bruto

        aux = self.ano_fim - self.ano_inicio + 1

        self.anos_vigencia = list(range(aux))

        for i in range(0, aux, 1):
            self.anos_vigencia[i] = str(self.ano_inicio + i)

    #def enviarirrfrecolhido(self):
    #    return self.irrf_recolhido

    def enviardadosparagrafico(self):

        return self.salario_liquido, self.irrf_recolhido, self.anos_vigencia, self.salario_base, (self.bonus_tempo + self.bonus_formacao + self.bonus_periculosidade), self.salario_base_de_calculo, self.total_deducoes

    def enviardadospararelatorio(self):

        return self.salario_base, self.salario_bruto, self.salario_base_de_calculo, self.anos_vigencia, self.salario_liquido, self.irrf_recolhido, self.aliquota_
