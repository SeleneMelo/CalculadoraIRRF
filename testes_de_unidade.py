import unittest
from LogicaCalculadora import LogicaCalculadora

    def setUp(self):
        # Configuração comum para os testes
        self.calculadora = LogicaCalculadora(salario_base=3000, bonus_tempo=500, bonus_formacao=200, bonus_periculosidade=100, mes_inicio=1, ano_inicio=2022, mes_fim=12, ano_fim=2022, numero_dependentes=2, pensao_alimenticia=200, outros_descontos=50, tipooferta='CLT')

    def test_calculo_bonus_e_salario_bruto(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(self.calculadora.bonus, 800)
        self.assertEqual(self.calculadora.salario_bruto, 3800)
      
    def test_calculo_deducoes_e_salario_base(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.assertEqual(self.calculadora.desconto_inss, 267.36)
        self.assertEqual(self.calculadora.desconto_dependente, 379.18)
        self.assertEqual(self.calculadora.total_deducoes, 846.54)
        self.assertEqual(self.calculadora.salario_base_de_calculo, 2953.46)
