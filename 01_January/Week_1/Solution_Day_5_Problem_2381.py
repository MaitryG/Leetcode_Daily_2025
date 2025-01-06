from typing import List


#Intuition: First we convert all chars in range 0,26.
# Brute force is O(n*m) so it is giving TLE.
# Better Approach is Prefix Sum: We keep an array prefix_diff which stores the number of shifts a range goes
# through, only difference is we will keep track of only the start and end indexes' shift changes, not all the
# numbers. See in notebook for detailed diagram and explanation.
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # lst = list(s)
        # print(lst)
        # for shift in shifts:
        #     for i in range(shift[0], shift[1]+1):
        #         if shift[2] == 0:
        #             if lst[i] == 'a':
        #                 lst[i] = 'z'
        #             else:
        #                 lst[i] = chr(ord(lst[i]) - 1)
        #         elif shift[2] == 1:
        #             if lst[i] == 'z':
        #                 lst[i] = 'a'
        #             else:
        #                 lst[i] = chr(ord(lst[i]) + 1)

        # return "".join(lst)

        prefix_diff = [0] * (len(s) + 1)
        for l, r, d in shifts:
            prefix_diff[r + 1] += 1 if d else -1
            prefix_diff[l] += -1 if d else 1

        diff = 0
        lst = [ord(c) - ord('a') for c in s]
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            lst[i - 1] = (diff + lst[i - 1]) % 26

        s = [chr(ord('a') + n) for n in lst]
        return "".join(s)

