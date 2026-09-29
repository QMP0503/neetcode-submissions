class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = [char for char in s if char.isalpha() or char.isdigit()]
        print(text)
        n = len(text)
        r , l = 0, n-1

        while r < l:
            if text[r].lower() != text[l].lower():
                return False
            else:
                r += 1
                l -= 1
        
        return True

        