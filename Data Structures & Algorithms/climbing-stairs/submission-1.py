class Solution:
    def climbStairs(self, n: int) -> int:
        count_one = 1
        count_two = 1
        for i in range(1, n):
            count_one, count_two = count_two, count_one + count_two
        return count_two