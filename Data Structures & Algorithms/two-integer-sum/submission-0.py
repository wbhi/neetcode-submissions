class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seem={}
        count=0
        for i in nums:
            j=target-i
            if j in seem:
                return [seem[j],count]
            seem[i]=count
            count+=1
        return [-1,-1]
            

        