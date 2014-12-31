import unittest

import calc


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = calc.Calculator(2)

    def test_add_when_arg_is_int(self):
        expected = 3
        actual = self.calculator.add(1)
        self.assertEqual(expected, actual)

    def test_add_when_arg_is_float(self):
        expected = 3.1
        actual = self.calculator.add(1.1)
        self.assertEqual(expected, actual)

    def test_add_when_arg_is_str(self):
        self.assertRaises(TypeError, self.calculator.add, '1')

    def test_add_when_arg_is_none(self):
        with self.assertRaises(Exception) as em:
            self.calculator.add(None)
        e = em.exception
        self.assertEqual("Arg should not be None.", str(e))


if __name__ == "__main__":
    unittest.main()
