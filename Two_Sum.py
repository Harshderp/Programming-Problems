from itertools import combinations            '''Importing combinations from itertools library'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):                  '''Loop through each element x and find if there is another value that equals to target - x.'''
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
