# Problem: You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range
# li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        strings = []
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        c = 0
        for i in range(len(words)):
            string = words[i]
            if string[0] in vowels and string[len(string) - 1] in vowels:
                c += 1

            strings.append(c)

        res = []
        for i in queries:
            if i[0] == 0:
                res.append(strings[i[1]])
            else:
                res.append(strings[i[1]] - strings[i[0] - 1
                                                   ])
        return res