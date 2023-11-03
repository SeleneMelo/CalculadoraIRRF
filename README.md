Calculadora de Imposto de Renda Retido na Fonte (IRRF) :bar_chart:
---

Trabalho Prático da disciplina de Engenharia de Software II da UFMG

## Dupla

- Gabriel Edmundo Rocha - 2020054412
- Selene Melo Andrade - 2019054986

## Explicação do sistema

O presente sistema é uma calculadora do IRRF (Imposto de renda retido na fonte). Ele possui uma interface visual em que o contribuinte entra com seu nome, CPF, informações de salário base, bonificações, periodicidade para a qual deseja calcular e eventuais descontos (dependentes, pensão alimenticia e outros). No modo "Grafico" serão entregues 3 gráficos: Um com seu salário básico e as bonificações, outro com seu salário base de cálculo e as deduções feitas para se chegar nele e o último com o valor de seu salário líquido e de seu IRRF (em reais por ano), o que forma o seu salário base para o calculo do IRRF. No modo "Relatório", o contribuinte tem um relatório com alguns dos valores totais das variáveis anteriormente referidas, além de sua aliquota efetiva de IRRF (valor do irrf/(salário base + bonificações) em porcentagem).
Além disso, o sistema suporta a entrada dos dados através de uma tabela (.xlxs), ao invés da interface gráfica, gerando vários relatórios ou gráficos para cada contribuinte (linha) da tabela.

## Tecnologias utilizadas

Para o desenvolvimento desse sistema optou-se por utilizar as seguintes tecnologias:

- **Linguagem de Programação**: Python
- **Bibliotecas**: PySimpleGUI, matplotlib, reportlab, numpy, pandas
- **Ferramenta de análise**: Lizard

## Explicação da ferramenta Lizard

A ferramenta realiza a análise de complexidade ciclomática do programa através de métricas para a quantidade de linhas não comentadas (NLOC), quantidade de caminhos de execução independentes do código fonte (CCN), quantidade de tokens e parâmetros utilizados e comprimento das funções.

Após rodar a ferramenta Lizard para todos os arquivos do sistema, obtivemos o seguinte relatório de complexidade:

    NLOC    CCN   token  PARAM  length  location  

      43      2    605      1      70   __init__@9-78@ClienteMultiUnitario.py
      40      6    861      1      55   criar_graficos_e_relatorios@81-135@ClienteMultiUnitario.py
     120     18   1117      0     155   interface_visual@122-276@InterfaceVisual.py
      19      1    109     13      23   __init__@15-37@LogicaCalculadora.py
      32     11    452      1      52   formulas_entrada@40-91@LogicaCalculadora.py
       2      1     43      1       3   enviardadosparagrafico@96-98@LogicaCalculadora.py
       2      1     33      1       3   enviardadospararelatorio@100-102@LogicaCalculadora.py
      13      1     68     10      17   __init__@7-23@RelatorioPDF.py
      34      1    373      1      42   gerarrelatorio@25-66@RelatorioPDF.py
      13      1     70     10      17   __init__@8-24@Grafico.py
       3      2     70      2       3   adddin@26-28@Grafico.py
       3      2     78      3       3   adddin2@30-32@Grafico.py
      20      1    248      1      31   criargrafico1@34-64@Grafico.py
      20      1    248      1      31   criargrafico2@66-96@Grafico.py
      20      1    248      1      31   criargrafico3@98-128@Grafico.py
    5 file analyzed.
    ===========================================================================================================
    !!!! Warnings (cyclomatic_complexity > 15 or length > 1000 or nloc > 1000000 or parameter_count > 100) !!!!
    ================================================
      NLOC    CCN   token  PARAM  length  location  
    ------------------------------------------------
       120     18   1117      0     155 interface_visual@122-276@InterfaceVisual.py
    ==========================================================================================
    Total nloc   Avg.NLOC  AvgCCN  Avg.token   Fun Cnt  Warning cnt   Fun Rt   nloc Rt
    ------------------------------------------------------------------------------------------
       516      25.6     3.3      308.2       15            1      0.07    0.31


## Identificação das funções mais complexas

- Funções com valor de CCN que ultrapassem o valor limite (CCN > 15), são funções complexas demais e, portanto, de difícil manutenibilidade e reuso.
- A mensagem de alerta indica que existe uma função complexa demais entre todas analisadas, a função interface_visual(), com CCN = 18, podendo ser uma boa candidata a refatoração.
- Embora não exceda o limite (CCN > 15), a função formulas_entrada() possui um valor relativamente alto, CCN = 11, e deve avaliada com atenção.

  O relatório em detalhes pode ser obtido [aqui](relatorioLizard.pdf) 

## Retafotações

1) https://github.com/SeleneMelo/CalculadoraIRRF/commit/754132fb8ec5e41659720951666f6bb45624e402
2) https://github.com/SeleneMelo/CalculadoraIRRF/commit/2005b1dca9a01caedc44bb443e0ce85487952ca8
3) https://github.com/SeleneMelo/CalculadoraIRRF/commit/24d4f38887ebbf54f5ea0611570402a73a7cbb8b
