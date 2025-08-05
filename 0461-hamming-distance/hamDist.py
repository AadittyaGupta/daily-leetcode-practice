class Solution:
    def int2binary(self, numb):
        result = ""
        
        while numb > 0:
            if numb % 2 == 1:
                result += "1"
            else:
                result += "0"
    
            numb = numb // 2

        result = result[::-1]
        return result
    
    def hammingDistance(self, x: int, y: int) -> int:

        ans = x ^ y

        num = self.int2binary(ans)

        count = 0

        for char in num:
            if char == "1":
                count += 1

        return count
        