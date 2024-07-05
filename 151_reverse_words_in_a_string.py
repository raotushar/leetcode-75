class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = ""

        s = s.split()
        end = len(s)-1

        while end >= 0:
            if s[end] != ' ':
                result += s[end] + ' '
            end -= 1
        return result[:-1]