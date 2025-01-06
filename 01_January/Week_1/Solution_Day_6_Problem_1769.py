from typing import List

# Approach: Simple differencing of index
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        indx = []
        for i in range(0, len(boxes)):
            if boxes[i] == "1":
                indx.append(i)

        for i in range(0, len(boxes)):
            s = 0
            for j in range(len(indx)):
                s += abs(indx[j] - i)

            res.append(s)

        return res