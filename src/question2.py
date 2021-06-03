class Orders:
    def combine_orders(self, requests: list[int], n_max: int) -> int:
        requests_copy = requests[:]
        trips_pair = []

        
        while requests_copy:
          
            highest_value = max(requests_copy)
            
            smallest_value = min(requests_copy)
            
            
            if len(requests_copy) == 1:
                trips_pair.append((requests_copy[0], 0))
                requests_copy.remove(requests_copy[0])


            elif (highest_value + smallest_value) <= n_max:
                trips_pair.append((highest_value, smallest_value))
                requests_copy.remove(highest_value)
                requests_copy.remove(smallest_value)
            
            else: 
                trips_pair.append((highest_value, 0))
                requests_copy.remove(highest_value)
            
        minimum_number_of_trips = len(trips_pair)
        
        return minimum_number_of_trips

            




orders = [11, 90,  70, 3, 41, 55]
n_max = 100
expected_orders = 3

how_many = Orders().combine_orders(orders, n_max)

assert how_many == expected_orders