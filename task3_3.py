class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=sum=0

        for current in nums:
            temp=max(sum,prev+current)
            prev=sum
            sum=temp
        return sum    