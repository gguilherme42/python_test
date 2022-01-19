class Orders:
    def combine_orders(self, requests: list[int], n_max: int) -> int:
        result = sorted(requests)
        total_trips = 0
        while True:
            if result:
                high_value = max(result)
                min_value = min(result)

                if len(result) > 1:
                    if (high_value + min_value) <= n_max:
                        total_trips += 1
                        result.remove(min_value)
                        result.remove(high_value)
                    else:
                        total_trips += 2
                else:
                    total_trips += 1
                    break
            else:
                break

        return total_trips

            