import unittest

import provider
from main import pos_sum, pos_sum2, pos_sum3, pos_sum1


class MyTestCase(unittest.TestCase):

    @data_provider(provider.Provider.pos_sum_1())
    def test_pos_sum(self, expected, found):
        res = pos_sum(found, len(found))
        self.assertEqual(expected, res, provider.Provider.msg_valores_diferentes())

    @data_provider(provider.Provider.expected_found())
    def test_pos_sum1(self, expected, found):
        res = pos_sum1(found)
        self.assertEqual(expected, res, provider.Provider.msg_valores_diferentes())

    @data_provider(provider.Provider.expected_found())
    def test_pos_sum2(self, expected, found):
        res = pos_sum2(found)
        self.assertEqual(expected, res, provider.Provider.msg_valores_diferentes())

    @data_provider(provider.Provider.expected_found())
    def test_pos_sum3(self, expected, found):
        res = pos_sum3(found)
        self.assertEqual(expected, res, provider.Provider.msg_valores_diferentes())

