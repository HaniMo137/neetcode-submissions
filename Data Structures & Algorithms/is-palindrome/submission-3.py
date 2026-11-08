class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(c for c in s if c.isalnum()).lower()
        for i in range(len(t)//2):
            if t[i] != t[-i-1]:
                return False
        return True
        