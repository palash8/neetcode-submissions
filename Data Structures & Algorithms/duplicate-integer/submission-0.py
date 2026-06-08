class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b=0
        seen={}
        for i in nums:
            seen[i]=b
            b=b+1
        if len(seen) != len(nums):
            return True
        else:
            return False

         