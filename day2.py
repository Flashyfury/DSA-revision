# Container with most water- You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1

        return max_area
                

  #testing      
obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))
        