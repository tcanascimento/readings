import unittest

from main import pos_sum, pos_sum2, pos_sum3, pos_sum1
from unittest_data_provider import data_provider
import provider
from pyunitreport import HTMLTestRunner

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



if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='test-reports'))
