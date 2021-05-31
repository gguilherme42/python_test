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
        
    contracts_not_renegotiated = [(contract.get_debt(), contract.get_id()) for contract in open_contracts 
                                    if contract.get_id() not in renegotiated_contracts]

    # Highest debtor to smallest debtor
    contracts_not_renegotiated.sort(reverse=True)

 
    max_contratcs_to_return = top_n if len(contracts_not_renegotiated) >= top_n else len(contracts_not_renegotiated) 

    top_n_contracts_not_renegotiated = [id  for debt, id in contracts_not_renegotiated[:max_contratcs_to_return] ]
 
    return top_n_contracts_not_renegotiated 




contracts_list = [
    Contract(1, 10),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3

actual_open_contracts = get_top_N_open_contracts(open_contracts=contracts_list, renegotiated_contracts=renegotiated, top_n=top_n)


print(actual_open_contracts)
expected_open_contracts = [1, 5, 4,]
assert expected_open_contracts == actual_open_contracts