class Orders:
    def combine_orders(self, requests: list[int], n_max: int) -> int:
        result = requests[:]
        trips_pair = []

        
        while result:
          
            highest_value = max(result)
            
            smallest_value = min(result)
            
            
            if len(result) == 1:
                trips_pair.append((result[0], 0))
                result.remove(result[0])


            elif (highest_value + smallest_value) <= n_max:
                trips_pair.append((highest_value, smallest_value))
                result.remove(highest_value)
                result.remove(smallest_value)
            
            else: 
                trips_pair.append((highest_value, 0))
                result.remove(highest_value)
            
        minimum_number_of_trips = len(trips_pair)
        
        return minimum_number_of_trips

            