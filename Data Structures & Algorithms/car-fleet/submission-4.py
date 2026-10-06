class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = 0
        max_dist = 0
        spd = {position[i]: speed[i] for i in range(len(position))}
        sorted_pos = sorted(position, reverse = True)
        ret = 0
        current_time = -1
        for i in range(len(position)):
            time = (target - sorted_pos[i]) / spd[sorted_pos[i]]
            if current_time == -1: 
                current_time = time
                ret += 1
                continue
            if time > current_time:
                #print(f"triggered at index {i}")
                current_time = time
                ret += 1
        return ret

    

