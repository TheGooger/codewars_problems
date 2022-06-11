import unittest


def persistence(num):
    res = 0
    num = str(num)
    while len(num) > 1:
        mult = 1
        for element in num:
            mult *= int(element)
        res += 1
        num = str(mult)
    return res


class ProblemTestCase(unittest.TestCase):

    def test_one_digit(self):
        result = persistence(4)
        self.assertEqual(result, 0)

    def test_two_digit(self):
        result = persistence(39)
        self.assertEqual(result, 3)

    def test_three_digit(self):
        result = persistence(999)
        self.assertEqual(result, 4)
