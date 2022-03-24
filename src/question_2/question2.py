class Orders:
    def combine_orders(self, requests: list[int], n_max: int) -> int:
        result = sorted(requests)
        minimum_trips = 0
        
        while result:    
            if len(result) > 1:
                high_value = result[-1]
                min_value = result[0]

                if (high_value + min_value) <= n_max:
                    minimum_trips += 1
                    result.remove(min_value)
                    result.remove(high_value)
                else:
                    minimum_trips += 1
                    result.remove(high_value) # It removes the high value because it doesn't have a pair, but the lowest could have.
                              
            else:
                minimum_trips += 1
                break
                
            

        return minimum_trips


orders = [70, 30, 10,]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)

assert how_many == expected_orders 