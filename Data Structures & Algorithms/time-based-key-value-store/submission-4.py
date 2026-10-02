class TimeMap:

    def __init__(self):
        self.sets = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.sets.keys():
            self.sets[key]=dict()
        if timestamp not in self.sets[key].keys():
            self.sets[key][timestamp] = ""
        self.sets[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        candidate_time = -1
        if key not in self.sets.keys(): return ""
        key_dict = self.sets[key]
        if timestamp in key_dict.keys(): return key_dict[timestamp]
        else:
            list_times = sorted(list(key_dict.keys()))
            l,r = 0, len(list_times)-1
            while l <= r:
                med = (l+r) // 2
                if list_times[med] < timestamp:
                    if list_times[med] > candidate_time: candidate_time = list_times[med]
                    l = med + 1
                else: r = med-1 
        return "" if candidate_time == -1 else key_dict[candidate_time]
