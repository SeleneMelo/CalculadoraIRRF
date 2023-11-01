from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor

class RelatorioPDF:

    def __init__(self, salario_base, salario_bruto, salario_base_de_calculo,
                anos_vigencia,
                salario_liquido, irrf_recolhido, aliquota,
                nome_contribuinte, cpf_contribuinte):

        self.salario_base = salario_base
        self.salario_bruto = salario_bruto
        self.salario_base_de_calculo = salario_base_de_calculo

        self.anos_vigencia            = anos_vigencia
        
        self.salario_liquido        = salario_liquido
        self.irrf_recolhido     = irrf_recolhido
        self.aliquota = aliquota
        
        self.nome_contribuinte                   = nome_contribuinte
        self.cpf_contribuinte                   =  cpf_contribuinte

    def gerarrelatorio(self):

        c = canvas.Canvas("Relatório de desconto de " + str(self.nome_contribuinte) + ".pdf", pagesize=(160*mm,160*mm))

        pc = list(range(2))

        anos_vigencia_aux = len(self.anos_vigencia)
        
        pc[0] = self.anos_vigencia[0]
        pc[1] = self.anos_vigencia[anos_vigencia_aux - 1]

        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 40)
        c.drawString(15,157,"Bem vindo contribuinte " + self.nome_contribuinte + " portador do CPF " + self.cpf_contribuinte + ".")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 18)
        c.drawString(15,92,"Seu salário base é de " + self.salario_bruto + " reais.")
        c.setFillColor(HexColor('#158d74'))
        c.setFont("Helvetica", 12)
        c.drawString(15,48,"Seu salário bruto, pós adição de bonificações é " + self.salario_bruto + " reais.")
        c.showPage()

        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 40)
        c.drawString(15,290,"A periodicidade começou em " + pc[0] + ".")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 18)
        c.drawString(260,307.5,"A periodicidade começou em " + pc[1] + ".")
        c.showPage()

        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 40)
        c.drawString(15,285, "Seu salário líquido pós IRRF é de " + self.salario_liquido + " reais.")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 18)
        c.drawString(155,290,"Seu IRRF ficou em " + self.irrf_recolhido + " reais.")
        c.setFillColor(HexColor('#158d74'))
        c.setFont("Helvetica", 12)
        c.drawString(350,310,"A aliquota efetiva ficou em " + (self.aliquota * 100) + "%.")
        c.showPage()

        c.save()