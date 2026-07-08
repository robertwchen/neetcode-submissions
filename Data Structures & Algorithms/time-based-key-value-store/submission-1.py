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
        t_list = self.t_map[key]
        for i in range(len(t_list) - 1, -1 , -1):
            value, prev_timestamp = t_list[i]
            if prev_timestamp <= timestamp:
                return value
        return ""
            

        
