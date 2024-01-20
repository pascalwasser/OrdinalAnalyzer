import unittest

from buchholz import PrincipalBuchholz, SumBuchholz, bh


class MyTestCase(unittest.TestCase):
    def test_principal_buchholz_zero(self):
        zero = PrincipalBuchholz("")
        self.assertEqual(len(zero.head), 0)
        self.assertEqual(len(zero.argument.sum_list), 0)
        self.assertEqual(zero.sequence, "")

    def test_principal_buchholz_one(self):
        one = PrincipalBuchholz("0")
        self.assertEqual(one.head, [0])
        self.assertEqual(len(one.argument.sum_list), 0)
        self.assertEqual(one.sequence, "0")

    def test_sum_buchholz_zero(self):
        zero = SumBuchholz([])
        self.assertEqual(len(zero.sum_list), 0)
        self.assertEqual(zero.sequence, "")

    def test_sum_buchholz_one(self):
        zero = SumBuchholz([PrincipalBuchholz("0")])
        self.assertEqual(len(zero.sum_list), 1)
        self.assertEqual(zero.sum_list[0].head, [0])
        self.assertEqual(zero.sequence, "0")

    def test_zero_equals_zero(self):
        self.assertEqual(bh.zero.compare(bh.zero), 0)

    def test_zero_smaller_one(self):
        self.assertEqual(bh.zero.compare(bh.one), -1)

    def test_one_greater_zero(self):
        self.assertEqual(bh.one.compare(bh.zero), 1)

    def test_one_equals_one(self):
        self.assertEqual(bh.one.compare(bh.one), 0)


if __name__ == '__main__':
    unittest.main()
