# -*- coding: utf-8 -*-

from .context import sample

import unittest


class CoreTestSuite(unittest.TestCase):
    """Test cases for Core"""

    def test_add(self):
        # SET-UP
        num1 = 1
        num2 = 2

        # EXECUTION
        result = sample.add(num1,num2)

        # ASSERT
        self.assertEqual(result, 3, "Los números no son iguales")

    def test_add_not_invalid_result(self):
        self.assertNotEqual(sample.add(1,2),3)


    def test_add_int_string(self):
        self.assertEqual(sample.add(1,'patata'),'1patata')

    def test_add_string_int(self):
        self.assertEqual(sample.add('patata', 1),'patata1')

    def test_add_int_float(self):
        self.assertEqual(sample.add(1, 2.1), 3.1)

    def test_add_float_int(self):
        self.assertEqual(sample.add(2.1, 1), 3.1)

    def test_add_bool_string(self):
        self.assertRaises(sample.add(True, 'hola'), TypeError)

    def test_add_string_bool(self):
        self.assertRaises(sample.add('hola', True), TypeError)

    def test_add_bool_bool(self):
        self.assertEqual(sample.add(True, True), True)



if __name__ == '__main__':
    unittest.main()
