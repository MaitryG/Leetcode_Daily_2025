class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        s = set()
        c = 0

        for i in range(len(A)):

            if A[i] not in s:
                s.add(A[i])
            else:
                c += 1

            if B[i] not in s:
                s.add(B[i])
            else:
                c += 1

            C.append(c)

        return C