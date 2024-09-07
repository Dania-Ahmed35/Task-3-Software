import math
class Solution:
    def getHours(self,piles,h,k):
        hrs=0
        for i in piles:
            hrs+=math.ceil(i/k)
        if(hrs<=h):
         return True
        else:
           return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         low=1
         high=max(piles)

         while low<high:
          mid=(low+high)//2
          if(self.getHours(piles,h,mid)):
            high=mid
          else: 
            low=mid+1 
         return low
