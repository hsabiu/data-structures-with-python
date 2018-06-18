import unittest
from applications import number_conversion


class TestNumberConversion(unittest.TestCase):

    def test_conversion_to_base_2(self):
        self.assertEquals(number_conversion.convert_base(25, 2), '11001')
        self.assertEquals(number_conversion.convert_base(250, 2), '11111010')
        self.assertEquals(number_conversion.convert_base(2500, 2), '100111000100')

    def test_conversion_to_base_8(self):
        self.assertEquals(number_conversion.convert_base(25, 8), '31')
        self.assertEquals(number_conversion.convert_base(250, 8), '372')
        self.assertEquals(number_conversion.convert_base(2500, 8), '4704')

    def test_conversion_to_base_16(self):
        self.assertEquals(number_conversion.convert_base(25, 16), '19')
        self.assertEquals(number_conversion.convert_base(250, 16), 'FA')
        self.assertEquals(number_conversion.convert_base(2500, 16), '9C4')

