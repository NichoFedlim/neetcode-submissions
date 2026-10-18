class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1 #index
        s = s.lower()

        # base case
        if len(s) == 0:
            return True

        while left < right:
            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -=1
                continue

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True