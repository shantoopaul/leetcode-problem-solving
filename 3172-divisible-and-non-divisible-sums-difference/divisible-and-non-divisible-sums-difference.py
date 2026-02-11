class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # num1 = []
        # num2 = []
        # for i in range(1, n + 1):
        #     num1.append(i) if i % m else num2.append(i)
        # return sum(num1) - sum(num2)

        # number of multiples of m up to n
        k = n // m
        # sum of n natural numbers
        num1 = n * (n + 1) // 2
        # sum of numbers divisible by m
        num2 = k * (k + 1) * m
        return num1 - num2