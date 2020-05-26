import unittest

from main import pos_sum, pos_sum2, pos_sum3, pos_sum1
from unittest_data_provider import data_provider
import mocks
from pyunitreport import HTMLTestRunner

class MyTestCase(unittest.TestCase):

    @data_provider(mocks.Mocks.expected_found())
    def test_pos_sum(self, expected, found):
        res = pos_sum(found, len(found))
        self.assertNotEqual(expected, res, mocks.Mocks.msg_valores_diferentes())

    @data_provider(mocks.Mocks.expected_found())
    def test_pos_sum1(self, expected, found):
        res = pos_sum1(found)
        self.assertEqual(expected, res, mocks.Mocks.msg_valores_diferentes())

    @data_provider(mocks.Mocks.expected_found())
    def test_pos_sum2(self, expected, found):
        res = pos_sum2(found)
        self.assertEqual(expected, res, mocks.Mocks.msg_valores_diferentes())

    @data_provider(mocks.Mocks.expected_found())
    def test_pos_sum3(self, expected, found):
        res = pos_sum3(found, 0)
        self.assertEqual(expected, res, mocks.Mocks.msg_valores_diferentes())



if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='test-reports'))
