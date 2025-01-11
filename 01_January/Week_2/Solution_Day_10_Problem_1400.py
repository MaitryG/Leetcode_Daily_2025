from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        res = []
        count = Counter(s)

        if len(s) < k:
            return False
        odd_chars = 0
        for a, c in count.items():
            if c % 2 != 0:
                odd_chars += 1

        if odd_chars > k:
            return False
        return True