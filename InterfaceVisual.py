# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from ClienteMultiUnitario import ClienteMultiUnitario
from Grafico import Grafico
from LogicaCalculadora import LogicaCalculadora
from RelatorioPDF import RelatorioPDF

desconto_medio_contrato = 0
montante_economizado_final = 0
periodo_de_contrato = list(range(2))

sg.theme('DarkBlue')

dados_salario = sg.Column([
    [sg.Frame('Dados sobre salário', [[sg.Text(), sg.Column([
        [sg.Text('Insira o seu salário base: ')],
        [sg.Input(key='Salario_Base', size=(19,1))],
        [sg.Text('Insira sua bonificação por tempo de serviço: ')],
        [sg.Input(key='Bonus_Tempo', size=(19,1))],
        [sg.Text('Insira sua bonificação por formação: ')],
        [sg.Input(key='Bonus_Formacao', size=(19,1))],
        [sg.Text('Insira seu adicional de periculosidade: ')],
        [sg.Input(key='Bonus_Periculosidade', size=(19,1))],
        [sg.Button('Upar dados do salário')]
        ], size=(340, 400), pad=(0,0))]])], ], pad=(0,0))

dados_salario_2 = sg.Column([
    [sg.Frame('Dados sobre salário', [[sg.Text(), sg.Column([
        [sg.Text('Insira o seu salário base: ')],
        [sg.Input(key='Salario_Base_2', size=(19,1))],
        [sg.Text('Insira sua bonificação por tempo de serviço: ')],
        [sg.Input(key='Bonus_Tempo_2', size=(19,1))],
        [sg.Text('Insira sua bonificação por formação: ')],
        [sg.Input(key='Bonus_Formacao_2', size=(19,1))],
        [sg.Text('Insira seu adicional de periculosidade: ')],
        [sg.Input(key='Bonus_Periculosidade_2', size=(19,1))],
        [sg.Button('Atualizar dados do salário')]
        ], size=(340, 400), pad=(0,0))]])], ], pad=(0,0))

inicio_fim = sg.Column([
    [sg.Frame('Tempo considerado para verificação', [[sg.Text(), sg.Column([
        [sg.Text('Digite o mês e o ano de início do calculo: ')],
        [sg.Input(key='Mes_Inicio', size=(19,1)),sg.Text('/'), sg.Input(key='Ano_Inicio', size=(19,1))],
        [sg.Text('Digite o mês e o ano de fim do calculo: ')],
        [sg.Input(key='Mes_Fim', size=(19,1)),sg.Text('/'), sg.Input(key='Ano_Fim', size=(19,1))],
        [sg.Button('Upar período de calculo')]
        ], size=(300, 400), pad=(0,0))]])], ], pad=(0,0))

inicio_fim_2 = sg.Column([
    [sg.Frame('Tempo considerado para verificação', [[sg.Text(), sg.Column([
        [sg.Text('Digite o mês e o ano de início do calculo: ')],
        [sg.Input(key='Mes_Inicio_2', size=(19,1)),sg.Text('/'), sg.Input(key='Ano_Inicio_2', size=(19,1))],
        [sg.Text('Digite o mês e o ano de fim do calculo: ')],
        [sg.Input(key='Mes_Fim_2', size=(19,1)),sg.Text('/'), sg.Input(key='Ano_Fim_2', size=(19,1))],
        [sg.Button('Atualizar período de calculo')]
        ], size=(300, 400), pad=(0,0))]])], ], pad=(0,0))

desconto_no_calculo = sg.Column([
    [sg.Frame('Descontos no calculo do IRRF', [[sg.Text(), sg.Column([
        [sg.Text('Digite o número de dependentes: ')],
        [sg.Input(key='ND', size=(19,1))],
        [sg.Text('Digite o valor de eventuais pensões alimentícias: ')],
        [sg.Input(key='PA', size=(19,1))],
        [sg.Text('Digite o valor de outras deduções: ')],
        [sg.Input(key='OD', size=(19,1))],
        [sg.Button('Upar descontos cabiveis no IRRF')]
        ], size=(300, 400), pad=(0,0))]])], ], pad=(0,0))

desconto_no_calculo_2 = sg.Column([
    [sg.Frame('Descontos no calculo do IRRF', [[sg.Text(), sg.Column([
        [sg.Text('Digite o número de dependentes: ')],
        [sg.Input(key='ND_2', size=(19,1))],
        [sg.Text('Digite o valor de eventuais pensões alimentícias: ')],
        [sg.Input(key='PA_2', size=(19,1))],
        [sg.Text('Digite o valor de outras deduções: ')],
        [sg.Input(key='OD_2', size=(19,1))],
        [sg.Button('Atualizar descontos cabiveis no IRRF')]
        ], size=(300, 400), pad=(0,0))]])], ], pad=(0,0))

layout_grafico = [sg.vtop([dados_salario, inicio_fim, desconto_no_calculo])]
layout_relatorio  = [sg.vtop([dados_salario_2, inicio_fim_2, desconto_no_calculo_2])]

layout = [[sg.Text('Clique no tipo de reposta que deseja obter: ')],
          [sg.Button('Gráfico'), sg.Button('Relatório')],
          [sg.Text('Digite seu o nome: ')],
          [sg.Input(key='Nome_Contribuinte', size=(38,1)), sg.Button('Adicionar nome')],
          [sg.Text('Digite o seu CPF: ')],
          [sg.Input(key='CPF_Contribuinte', size=(38,1)), sg.Button('Adicionar CPF')],
          [sg.Column(layout_grafico, visible=True, key='-COL1-'), sg.Column(layout_relatorio, visible=False, key='-COL2-')],
          ]

base_layout = [[sg.Text('Clique no tipo de operação que deseja efetuar: ')],
               [sg.Button('Entrar com seus dados via interface visual')],
               [sg.Button('Entrar com dados de múltiplas pessoas através de uma tabela')]]

window = sg.Window('Calculadora de IRRF', base_layout)
window_visual_interface = sg.Window('Calculadora de IRRF', layout)

nome_contribuinte = " "
cpf_contribuinte = " "

salario_base               = 0
bonus_tempo              = 0
bonus_formacao              = 0
bonus_periculosidade             = 0

mes_inicio   = 0
ano_inicio   = 0
mes_fim      = 0
ano_fim      = 0
anos_vigencia_aux = 0

numero_dependentes    = 0
pensao_alimenticia     = 0
outros_descontos       = 0
tipooferta           = 0

mg = 0
mr = 0

def interface_visual():

    while True:

        event, values = window_visual_interface.read()

        if event == sg.WIN_CLOSED:
            break

        if event =='Gráfico':
            window_visual_interface['-COL1-'].update(visible=True)
            window_visual_interface['-COL2-'].update(visible=False)
            mg = 1

        elif event == 'Relatório':
            window_visual_interface['-COL2-'].update(visible=True)
            window_visual_interface['-COL1-'].update(visible=False)
            mr = 1

        elif event == 'Adicionar nome':
            nome_contribuinte = str(values['Nome_Contribuinte'])

        elif event == 'Adicionar CPF':
            cpf_contribuinte = str(values['CPF_Contribuinte'])

        elif event =='Upar dados do salário':
            salario_base             = float(values['Salario_Base'])
            bonus_tempo              = float(values['Bonus_Tempo'])
            bonus_formacao           = float(values['Bonus_Formacao'])
            bonus_periculosidade     = float(values['Bonus_Periculosidade'])

        elif event =='Atualizar dados do salário':
            salario_base             = float(values['Salario_Base_2'])
            bonus_tempo              = float(values['Bonus_Tempo_2'])
            bonus_formacao           = float(values['Bonus_Formacao_2'])
            bonus_periculosidade     = float(values['Bonus_Periculosidade_2'])

        elif event =='Upar período de calculo':
            mes_inicio   = int(values['Mes_Inicio'])
            ano_inicio   = int(values['Ano_Inicio'])
            mes_fim      = int(values['Mes_Fim'])
            ano_fim      = int(values['Ano_Fim'])
            anos_vigencia_aux = ano_fim - ano_inicio + 1

        elif event =='Atualizar período de calculo':
            mes_inicio   = int(values['Mes_Inicio_2'])
            ano_inicio   = int(values['Ano_Inicio_2'])
            mes_fim      = int(values['Mes_Fim_2'])
            ano_fim      = int(values['Ano_Fim_2'])
            anos_vigencia_aux = ano_fim - ano_inicio + 1

        elif event =='Upar descontos cabiveis no IRRF':

            tipooferta             = 1
            numero_dependentes     = int(values['ND'])
            pensao_alimenticia     = float(values['PA'])
            outros_descontos       = float(values['OD'])

            logicacalculadora = LogicaCalculadora(salario_base, bonus_tempo, bonus_formacao, bonus_periculosidade,
            mes_inicio,ano_inicio,mes_fim,ano_fim,
            numero_dependentes,pensao_alimenticia,outros_descontos,tipooferta)

            logicacalculadora.formulas_entrada()

            anos_vigencia = list(range(anos_vigencia_aux))

            salario_liquido, irrf_recolhido, anos_vigencia, salario_base, adicoes, salario_base_de_calculo, total_deducoes = logicacalculadora.enviardadosparagrafico()

            salario_liquido_list         = list(range(anos_vigencia_aux))
            irrf_recolhido_list          = list(range(anos_vigencia_aux))
            salario_base_list            = list(range(anos_vigencia_aux))
            adicoes_list                 = list(range(anos_vigencia_aux))
            salario_base_de_calculo_list = list(range(anos_vigencia_aux))
            total_deducoes_list          = list(range(anos_vigencia_aux))

            if(anos_vigencia_aux == 1):
                salario_liquido_list[0]         = salario_liquido         * (mes_fim - mes_inicio + 1)
                irrf_recolhido_list[0]          = irrf_recolhido          * (mes_fim - mes_inicio + 1)
                salario_base_list[0]            = salario_base            * (mes_fim - mes_inicio + 1)
                adicoes_list[0]                 = adicoes                 * (mes_fim - mes_inicio + 1)
                salario_base_de_calculo_list[0] = salario_base_de_calculo * (mes_fim - mes_inicio + 1)
                total_deducoes_list[0]          = total_deducoes          * (mes_fim - mes_inicio + 1)

            elif(anos_vigencia_aux > 1):
                salario_liquido_list[0]         = salario_liquido         * (12 - mes_inicio + 1)
                irrf_recolhido_list[0]          = irrf_recolhido          * (12 - mes_inicio + 1)
                salario_base_list[0]            = salario_base            * (12 - mes_inicio + 1)
                adicoes_list[0]                 = adicoes                 * (12 - mes_inicio + 1)
                salario_base_de_calculo_list[0] = salario_base_de_calculo * (12 - mes_inicio + 1)
                total_deducoes_list[0]          = total_deducoes          * (12 - mes_inicio + 1)

                for i in range(1, (anos_vigencia_aux - 1), 1):
                    salario_liquido_list[i]         = salario_liquido         * 12
                    irrf_recolhido_list[i]          = irrf_recolhido          * 12
                    salario_base_list[i]            = salario_base            * 12
                    adicoes_list[i]                 = adicoes                 * 12
                    salario_base_de_calculo_list[i] = salario_base_de_calculo * 12
                    total_deducoes_list[i]          = total_deducoes          * 12

                salario_liquido_list[anos_vigencia_aux - 1]         = salario_liquido         * mes_fim
                irrf_recolhido_list[anos_vigencia_aux - 1]          = irrf_recolhido          * mes_fim
                salario_base_list[anos_vigencia_aux - 1]            = salario_base            * mes_fim
                adicoes_list[anos_vigencia_aux - 1]                 = adicoes                 * mes_fim
                salario_base_de_calculo_list[anos_vigencia_aux - 1] = salario_base_de_calculo * mes_fim
                total_deducoes_list[anos_vigencia_aux - 1]          = total_deducoes          * mes_fim


            grafico = Grafico(salario_liquido_list, irrf_recolhido_list, anos_vigencia, -1,
                              salario_base_list, adicoes_list,
                              salario_base_de_calculo_list, total_deducoes_list,
                              nome_contribuinte)

            grafico.criargrafico1()
            grafico.criargrafico2()
            grafico.criargrafico3()

        elif event =='Atualizar descontos cabiveis no IRRF':

            tipooferta = 2
            numero_dependentes     = int(values['ND_2'])
            pensao_alimenticia     = float(values['PA_2'])
            outros_descontos       = float(values['OD_2'])

            logicacalculadora = LogicaCalculadora(salario_base, bonus_tempo, bonus_formacao, bonus_periculosidade,
            mes_inicio,ano_inicio,mes_fim,ano_fim,
            numero_dependentes,pensao_alimenticia,outros_descontos,tipooferta)

            logicacalculadora.formulas_entrada()

            salario_base, salario_bruto, salario_base_de_calculo, anos_vigencia, salario_liquido, irrf_recolhido, aliquota_ = logicacalculadora.enviardadospararelatorio()

            if(anos_vigencia_aux == 1):
                salario_base = salario_base * (mes_fim - mes_inicio + 1)
                salario_bruto = salario_bruto * (mes_fim - mes_inicio + 1) 
                salario_base_de_calculo = salario_base_de_calculo * (mes_fim - mes_inicio + 1)
                salario_liquido = salario_liquido * (mes_fim - mes_inicio + 1)
                irrf_recolhido  = irrf_recolhido * (mes_fim - mes_inicio + 1)
                aliquota_ = irrf_recolhido/salario_bruto

            elif(anos_vigencia_aux > 1):
                salario_base = salario_base * ((12 - mes_inicio + 1) + ((anos_vigencia_aux - 2) * 12) + (mes_fim))
                salario_bruto = salario_bruto * ((12 - mes_inicio + 1) + ((anos_vigencia_aux - 2) * 12) + (mes_fim))
                salario_base_de_calculo = salario_base_de_calculo * ((12 - mes_inicio + 1) + ((anos_vigencia_aux - 2) * 12) + (mes_fim))
                salario_liquido = salario_liquido * ((12 - mes_inicio + 1) + ((anos_vigencia_aux - 2) * 12) + (mes_fim))
                irrf_recolhido  = irrf_recolhido * ((12 - mes_inicio + 1) + ((anos_vigencia_aux - 2) * 12) + (mes_fim))
                aliquota_ = irrf_recolhido/salario_bruto

            relatoriopdf = RelatorioPDF(salario_base, salario_bruto, salario_base_de_calculo,
                anos_vigencia,
                salario_liquido, irrf_recolhido, aliquota_,
                nome_contribuinte, cpf_contribuinte)

            relatoriopdf.gerarrelatorio()

    window_visual_interface.close()

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Entrar com dados de múltiplas pessoas através de uma tabela':

        clientemultiunitario = ClienteMultiUnitario()

        clientemultiunitario.prencher_variaveis_multiplas()

        clientemultiunitario.criar_graficos_e_relatorios()

        window.close()

    elif event == 'Entrar com seus dados via interface visual':

        interface_visual()
