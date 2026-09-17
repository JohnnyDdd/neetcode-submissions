class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        s_dict = {}
        for a in list_s:
            if a not in s_dict.keys(): s_dict[a] = 1
            else: s_dict[a] += 1
        for c in list_t:
            if c not in s_dict.keys(): return False
            else: s_dict[c] -= 1
        
        return s_dict == {a:0 for a in list_s}