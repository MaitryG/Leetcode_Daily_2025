class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def numberOfBits(num):
            cnt = 0

            while num:
                cnt += num % 2
                num = num >> 1

            return cnt

        cnt1 = numberOfBits(num1)
        cnt2 = numberOfBits(num2)

        x = num1
        i = 0

        while cnt1 > cnt2:
            if x & (1 << i):
                cnt1 -= 1
                x = x ^ (1 << i)
            i += 1

        while cnt1 < cnt2:
            if x & (1 << i) == 0:
                cnt1 += 1
                x = x | (1 << i)
            i += 1

        return x
