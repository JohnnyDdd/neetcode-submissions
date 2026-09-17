class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.split('[^a-zA-Z0-9]',s)
        s = ''.join(s).lower()
        print(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]: return False
            i+=1
            j-=1
        return True