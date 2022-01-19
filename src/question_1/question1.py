class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def get_id(self) -> int:
        return self.id
    
    def get_debt(self) -> float:
        return self.debt
    

    def __str__(self):
        return f"id={self.id}, debt={self.debt}"


def get_top_N_open_contracts(open_contracts: list[Contract], renegotiated_contracts: list[int], top_n: int) -> list[int]:

    def not_renegotiated(contract: Contract):
        if contract.get_id() not in renegotiated_contracts:
            return contract.get_debt(), contract.get_id()
    

    result = list(filter(not_renegotiated, open_contracts))

    number_of_contracts_to_return = top_n if len(result) >= top_n else len(result) 

    result = sorted(result, key=lambda contract: contract.get_debt(), reverse=True)[:number_of_contracts_to_return]

    return [contract.get_id() for contract in result]




contracts_list = [
    Contract(1, 10),
    Contract(2, 100),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 20)
]
renegotiated = [3, 4]

top_n = 3

actual_open_contracts = get_top_N_open_contracts(open_contracts=contracts_list, renegotiated_contracts=renegotiated, top_n=top_n)

expected_open_contracts = [2, 5, 1]
assert expected_open_contracts == actual_open_contracts