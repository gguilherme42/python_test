class Contract:
    def __init__(self, id: int, debt: float):
        self.id = id
        self.debt = debt


def get_top_N_open_contracts(open_contracts: list[Contract], renegotiated_contracts: list[int], top_n: int) -> list[int]:
    renegotiated = set(renegotiated_contracts)

    def not_renegotiated(contract: Contract):
        if contract.id not in renegotiated:
            return contract
    
    result = filter(not_renegotiated, open_contracts)

    result = sorted(result, key=lambda contract: contract.debt, reverse=True)

    number_of_contracts_to_return = top_n if len(result) >= top_n else len(result) 

    return [contract.id for contract in result[:number_of_contracts_to_return]]




contracts_list = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3

actual_open_contracts = get_top_N_open_contracts(contracts_list, renegotiated, top_n)

expected_open_contracts = [5,4,2]
assert expected_open_contracts == actual_open_contracts