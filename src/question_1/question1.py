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
    


class Contracts:
    def get_top_N_open_contracts(self, open_contracts: list[Contract], renegotiated_contracts: list[int], top_n: int) -> list[int]:
            
        renegotiated_set = {*renegotiated_contracts}

        contracts_not_renegotiated = [(contract.get_debt(), contract.get_id(), ) for contract in open_contracts 
                                        if contract.get_id() not in renegotiated_set]

        number_of_contracts_to_return = top_n if len(contracts_not_renegotiated) >= top_n else len(contracts_not_renegotiated) 

        ordered_contracts = sorted(contracts_not_renegotiated,reverse=True)[:number_of_contracts_to_return]

        top_n_contracts = [id for debt, id in ordered_contracts]


        return top_n_contracts




contracts_list = [
    Contract(1, 10),
    Contract(2, 100),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 20)
]
renegotiated = [3, 4]

top_n = 3

actual_open_contracts = Contracts().get_top_N_open_contracts(open_contracts=contracts_list, renegotiated_contracts=renegotiated, top_n=top_n)


print(actual_open_contracts)
expected_open_contracts = [2, 5, 1]
assert expected_open_contracts == actual_open_contracts