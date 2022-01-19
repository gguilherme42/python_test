import unittest

from question2 import Orders


class TestQuestion2(unittest.TestCase):
    def setUp(self):
        self.orders = [11, 90,  70, 3, 41, 55]
        self.n_max = 100
        self.expected_orders = 2
        

    def test_when_the_expected_order_is_2_and_n_max_is_100(self):
        how_many = Orders().combine_orders(self.orders, self.n_max)

        self.assertEqual(how_many, self.expected_orders)


if __name__ == "__main__":
    unittest.main()