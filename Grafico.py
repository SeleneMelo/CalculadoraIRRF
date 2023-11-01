import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.patches as mpatches
import numpy as np

class Grafico:

    def __init__(self, salario_liquido, irrf_recolhido, anos_vigencia, numero_de_graficos, nome_contribuinte):

        self.salario_liquido    = salario_liquido
        self.irrf_recolhido     = irrf_recolhido
        self.anos_vigencia      = anos_vigencia
        self.numero_de_graficos = numero_de_graficos + 1
        self.nome_contribuinte  = nome_contribuinte


    def criargrafico(self):

        plt.rc('font', **{'sans-serif' : 'Arial',
                            'family' : 'sans-serif'})

        fig, ax = plt.subplots()

        plt.title('Valor do salário líquido e do IRRF em X anos')

        plt.xlabel(u'Anos de contribuição')
        plt.ylabel(u'Valores anuais')

        plt.bar(self.anos_vigencia, self.salario_liquido,color=(.078, .55, .455))
        plt.bar(self.anos_vigencia, self.irrf_recolhido,color=(.502, .780, .228),bottom=np.array(self.salario_liquido))

        red_patch = mpatches.Patch(color=(.078, .55, .455), label='Salário Líquido')

        blue_patch = mpatches.Patch(color=(.502, .780, .228), label='Imposto de Renda Retido na Fonte')

        ax.legend(handles=[red_patch, blue_patch])

        fmt = "R${x:.0f}"
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)

        def adddin(x,y):
            for i in range(len(x)):
                plt.text(i, y[i]/2, 'R${:,.2f}'.format(y[i]).replace(",", "X").replace(".", ",").replace("X", "."), ha = 'center', rotation=90)

        def adddin2(x,yp,y):
            for i in range(len(x)):
                plt.text(i, 1.1*yp[i], 'R${:,.2f}'.format(y[i]).replace(",", "X").replace(".", ",").replace("X", "."), ha = 'center', rotation=60, wrap=True)

        adddin(self.anos_vigencia, self.salario_liquido)
        adddin2(self.anos_vigencia, self.salario_liquido, self.irrf_recolhido)

        fig = plt.gcf()
        plt.show()
        fig.savefig('grafico do contribuinte ' + str(self.nome_contribuinte) +'.png', format='png')