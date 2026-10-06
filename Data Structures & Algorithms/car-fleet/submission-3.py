class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = 0
        max_dist = 0
        spd = {position[i]: speed[i] for i in range(len(position))}
        sorted_pos = sorted(position, reverse = True)
        ret = 0
        stack = []
        for i in range(len(position)):
            time = (target - sorted_pos[i]) / spd[sorted_pos[i]]
            if not stack: 
                stack.append(time)
                ret += 1
                continue
            current = stack[-1]
            if time > current:
                #print(f"triggered at index {i}")
                stack.append(time)
                ret += 1
        return ret

    

