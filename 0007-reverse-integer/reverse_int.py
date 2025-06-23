class Solution:
    def reverse(self, x: int) -> int:
        min_int = - 2**31
        max_int = 2**31 - 1
        rev = 0
        sigh = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            #checking for overflow
            if rev > (max_int - digit) // 10:
                return 0

            rev = rev * 10 + digit   

        return sigh * rev   