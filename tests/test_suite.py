# -*- coding: utf-8 -*-
import unittest                                                                                                       

from tests import test_calc, test_random


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # テストメソッド単位で追加
    suite.addTest(test_calc.TestCalculator('test_add_when_arg_is_int'))
    # テストクラス単位で追加
    suite.addTest(unittest.makeSuite(test_calc.TestCalculator))
    suite.addTest(loader.loadTestsFromTestCase(test_calc.TestCalculator))
    # テストモジュール単位で追加
    suite.addTest(loader.loadTestsFromModule(test_random))
    # テストスイートを実行
    unittest.TextTestRunner(verbosity=2).run(suite)
