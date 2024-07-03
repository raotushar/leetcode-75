from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candy = max(candies)
        result = [True if i+extraCandies>=max_candy else False for i in candies]
        return result