class Solution:
    def int2binary(self, num):
        result = ""

        while num > 0:
            if num % 2 == 1:
                result += "1"
            else:
                result += "0"

            num = num // 2

        result = result[::-1]
        return result

    def minBitFlips(self, start: int, goal: int) -> int:

        ans = start ^ goal

        ans2 = self.int2binary(ans)

        count = 0
        
        for char in ans2:
            if char == '1':
                count += 1

        return count

