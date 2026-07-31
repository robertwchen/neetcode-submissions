from collections import defaultdict
class TimeMap:
    # store array tuple? or hashmap?
    # for constructor no parameter just setup the ds
    # for set gotta just set value 
    # why not just make key (key, timestamp):
    # for get have to retrieve 

    def __init__(self):
        self.t_map = defaultdict(list)
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.t_map[key].append((value, timestamp))
        return
        

    def get(self, key: str, timestamp: int) -> str:
        # find the key value pair quickly maybe do bs on hashmap
        value_list = self.t_map[key]
        result = ""

        left = 0
        right = len(value_list) - 1
        while left <= right:
            
            mid = (left + right) // 2
            if timestamp == value_list[mid][1]:
                return value_list[mid][0]

            elif timestamp > value_list[mid][1]:
                result = value_list[mid][0]
                left = mid + 1
            
            elif timestamp < value_list[mid][1]:
                right = mid - 1
        
        return result

            

        
