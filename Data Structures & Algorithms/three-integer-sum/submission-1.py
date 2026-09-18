class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(nums)
        list_trip = []
        num_visited = set()
        for index in range(n):
            x = sorted_nums[index]
            i = index + 1 
            j = n - 1
            visited = set()
            if x not in num_visited:
                while i < j:
                    y = sorted_nums[i]
                    z = sorted_nums[j]
                    sum = y + z
                    # y <= z
                    if y + z == -x and y not in visited and z not in visited: 
                        list_trip.append([x,y,z])
                        visited.add(y)
                        visited.add(z)
                        i += 1
                    elif y + z > -x:
                        j -= 1
                    else: i += 1
                num_visited.add(x)
        return list_trip