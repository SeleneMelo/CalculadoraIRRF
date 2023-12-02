import unittest
from LogicaCalculadora import LogicaCalculadora

class TestLogicaCalculadora(unittest.TestCase):

    def setUp(self):
        # Configuração comum para os testes
        self.calculadora = LogicaCalculadora(salario_base=3000, bonus_tempo=500, bonus_formacao=200, bonus_periculosidade=100,
                                             mes_inicio=1, ano_inicio=2022, mes_fim=12, ano_fim=2022,
                                             numero_dependentes=2, pensao_alimenticia=200, outros_descontos=50, tipooferta='CLT')

    def test_calculo_bonus_e_salario_bruto(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.assertEqual(self.calculadora.bonus, 800)
        self.assertEqual(self.calculadora.salario_bruto, 3800)

    def test_calculo_irrf_recolhido_salario_liquido_aliquota(self):
        self.calculadora.calculo_bonus_e_salario_bruto()
        self.calculadora.calculo_deducoes_e_salario_base()
        self.calculadora.calculo_irrf_recolhido_salario_liquido_aliquota()
        self.assertEqual(self.calculadora.irrf_recolhido, 33.35)
        self.assertEqual(self.calculadora.salario_liquido, 2920.11)
        self.assertAlmostEqual(self.calculadora.aliquota_, 0.00876, places=5)

    def test_definir_anos_vigencia(self):
        self.calculadora.definir_anos_vigencia()
        self.assertEqual(self.calculadora.anos_vigencia, ['2022'])

if __name__ == '__main__':
    unittest.main()

