class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n in (0,1): return n
        alphabet = set(list(s))
        l,r = 0,0
        ret = 0

        presence = {a:0 for a in alphabet}
        loc_max = 0
        while r < n:
            if presence[s[r]] == 0: 
                #print("PASS")
                presence[s[r]] += 1
                loc_max += 1
            else: 
                #print(f"rep discovered at {r}")
                ret = max(ret, loc_max)
                presence[s[r]] += 1
                loc_max += 1
                while presence[s[r]] > 1:
                    #print(f"removing {l}") 
                    presence[s[l]] -= 1
                    loc_max -= 1
                    l += 1
            r += 1
        #print(presence)
        return max(ret, loc_max)