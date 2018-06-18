import unittest
from applications import expressions


class TestExpressions(unittest.TestCase):

    def test_evaluate_postfix(self):
        self.assertEqual(expressions.evaluate_postfix("1 2 + 3 4 + +"), 10.0)
        self.assertEqual(expressions.evaluate_postfix("7 8 + 3 2 + /"), 3.0)

    def test_evaluate_prefix(self):
        self.assertEqual(expressions.evaluate_prefix("+ + 1 2 + 3 4"), 10.0)
        self.assertEqual(expressions.evaluate_prefix("/ + 7 8 + 3 2"), 3.0)
