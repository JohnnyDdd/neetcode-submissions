class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles)        
        if h == len(piles): return sorted_piles[-1]
        l,r = 1, sorted_piles[-1]

        # start with upper bound
        ret = r

        while l <= r:
            mid_eff = math.ceil((l+r) / 2)
            test_hrs = sum([math.ceil(pile/mid_eff) for pile in piles])
            if test_hrs <= h:
                r = mid_eff - 1
                ret = mid_eff
            else: l = mid_eff + 1
        return ret