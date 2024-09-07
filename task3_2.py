from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge=[]
        intervals.sort(key=lambda x: x[0])
        prev=intervals[0]
        for current in intervals[1:]:
            if prev[1]>=current[0]:
              prev[1] = max(prev[1], current[1])

            else:
                merge.append(prev)  
                prev=current

        merge.append(prev)
        return merge
