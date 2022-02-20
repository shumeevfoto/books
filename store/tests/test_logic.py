from unittest import TestCase

from store.logic import operations


class TestOperation(TestCase):
    def test_Plus(self):
        result = operations(2, 6, '+')
        self.assertEqual(8, result)
