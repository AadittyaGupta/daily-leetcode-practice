class Solution:
    def fibo(self,num):
        if num == 0 or num ==1:
            return num

        return self.fibo(num-1) + self.fibo(num-2)

    def fib(self, n: int) -> int:
        ans = self.fibo(n)
        return ans