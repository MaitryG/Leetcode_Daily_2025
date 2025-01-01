# Problem: Given a string s of zeros and ones, return the maximum score after splitting the
# string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the
# number of ones in the right substring.

# Intuition: Used brute force, looped over the string and on each iteration, performed a split and
# created left and the right substrings. Checked number of zeros in left substring and number of ones
# right substring and calculated the scores.

class Solution:
    def maxScore(self, s: str) -> int:
        def check_zeros(left_str):
            count = 0
            for i in range(len(left_str)):
                if left_str[i] == '0':
                    count += 1

            return count

        def check_ones(right_str):
            count = 0
            for i in range(len(right_str)):
                if right_str[i] == '1':
                    count += 1

            return count

        score = 0
        for i in range(len(s) - 1):
            left_str = s[:i + 1]
            right_str = s[i + 1:]
            score_left = check_zeros(left_str)
            score_right = check_ones(right_str)
            score = max(score, score_left + score_right)

        return score