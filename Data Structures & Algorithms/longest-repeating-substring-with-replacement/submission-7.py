class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ret = k + 1
        freq = {a:0 for a in s}
        window_width = len(s) - k
        for r in range(len(s)):
            print(l,r)
            while (r - l) - max(freq.values()) > k : 
                freq[s[l]] -= 1
                l += 1
            freq[s[r]] += 1
            ret = max(max(freq.values()) + k, ret)
        return min(ret, len(s))