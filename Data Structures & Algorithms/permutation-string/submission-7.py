class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_s1 = {}
        for s in s1: 
            d_s1[s] = d_s1.get(s,0) + 1

        d_s2 = {}
        l = 0
        n = len(s1)
        for r in range(len(s2)):
            if s2[r] in d_s1.keys():
                while d_s2.get(s2[r],0) >= d_s1[s2[r]]:
                    if s2[l] in d_s1.keys(): d_s2[s2[l]] -= 1
                    l += 1
                d_s2[s2[r]] = d_s2.get(s2[r],0) + 1
            else:
                d_s2 = {}
            if d_s2 == d_s1: return True
        return d_s2 == d_s1