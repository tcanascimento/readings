import unittest

from main import pos_sum, pos_sum2, pos_sum3
import mocks

class MyTestCase(unittest.TestCase):

    def test_pos_sum_erro(self):
        res = pos_sum(mocks.Mocks.lista_base(), len(mocks.Mocks.lista_base()))
        self.assertNotEqual(10, res, "Valores diferentes!")

    def test_pos_sum_vazio(self):
        res = pos_sum(mocks.Mocks.lista_vazia(), len(mocks.Mocks.lista_vazia()))
        self.assertEqual(0, res, "Erro em lista vazia!")

    def test_pos_sum2_erro(self):
        res = pos_sum2(mocks.Mocks.lista_base())
        self.assertEqual(10, res, "Valores diferentes!")

    def test_pos_sum2_vazio(self):
        res = pos_sum2(mocks.Mocks.lista_vazia())
        self.assertEqual(0, res, "Erro em lista vazia!")

    def test_pos_sum3_erro(self):
        res = pos_sum3(mocks.Mocks.lista_base(), 0)
        self.assertEqual(10, res, "Valores diferentes!")

    def test_pos_sum3_vazio(self):
        res = pos_sum3(mocks.Mocks.lista_vazia(), 0)
        self.assertEqual(0, res, "Erro em lista vazia!")


if __name__ == '__main__':
    unittest.main()
