class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        n = len(s)
        
        dt = {}
        for a in t:
            dt[a] = dt.get(a,0) + 1
        
        dr = {key:0 for key in dt.keys()}

        l = 0
        count = 0
        for r in range(n):
            if s[r] in dt.keys():
                dr[s[r]] += 1
                if dr[s[r]] <= dt[s[r]]: count += 1
                print(count)
            if count == len(t):
                while count == len(t):
                    if s[l] in dr.keys(): 
                        dr[s[l]] -= 1 
                        if dr[s[l]] < dt[s[l]]: count -= 1
                    l += 1
                ret = s[l-1:r + 1] if (len(ret) == 0 or len(ret) > r-l+1) else ret
        return ret

