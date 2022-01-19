import unittest
from question1 import Contract, get_top_N_open_contracts

class Question1Test(unittest.TestCase):
    def setUp(self):
        self.contracts_list = [
            Contract(1, 10),
            Contract(2, 100),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 20)
        ]
    
    def test_when_theres_one_renegotiaded_contract(self):
        renegotiated = [3,]
        top_n = 3
        actual_open_contracts = get_top_N_open_contracts(self.contracts_list, renegotiated, top_n)

        expected_open_contracts = [2, 5, 1]
        self.assertEqual(expected_open_contracts, actual_open_contracts)
    
    def test_when_there_are_no_renegotiated_contracts_and_top_n_is_four(self):
        renegotiated = []
        top_n = 4
        actual_open_contracts = get_top_N_open_contracts(self.contracts_list, renegotiated, top_n)

        expected_open_contracts = [2, 5, 1, 4]
        self.assertEqual(expected_open_contracts, actual_open_contracts)

    def test_when_there_are_no_open_contracts(self):
        renegotiated = [1,2,3,4,5]
        top_n = 3
        actual_open_contracts = get_top_N_open_contracts(self.contracts_list, renegotiated, top_n)

        expected_open_contracts = []
        self.assertEqual(expected_open_contracts, actual_open_contracts)


if __name__ == "__main__":
    unittest.main()