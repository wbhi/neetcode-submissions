class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,i in enumerate(nums):
            j=target-i
            if j in seen:
                return [seen[j], index]
            seen[i]=index
        return [-1,-1]


        