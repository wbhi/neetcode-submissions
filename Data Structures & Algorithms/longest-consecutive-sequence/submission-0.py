class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set()
        i=0
        while(i<len(nums)):
            if nums[i]-1 in nums:
                i+=1
            else:
                curr_set=set()
                curr_set.add(nums[i])
                j=1
                while(True):
                    if nums[i]+j in nums:
                        curr_set.add(nums[i]+j)
                        j+=1
                    else:
                        break
                if len(curr_set)>len(num_set):
                    num_set=curr_set
                i+=1
        return len(num_set)


                    
                    

        



        