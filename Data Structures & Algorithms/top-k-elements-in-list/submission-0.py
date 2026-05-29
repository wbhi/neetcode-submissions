class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for i in count.keys():
            index=count[i]
            buckets[index].append(i)
        res=[]
        for i in reversed(buckets):
            if len(res)<k and len(i)>=1:
                res.extend(i)
        return res

