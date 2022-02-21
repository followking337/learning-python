print('\n1295. Find Numbers with Even Number of Digits')
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even = 0
        for i in [str(i) for i in nums]:
            even += not len(i) % 2
        return even


s = Solution()

a = [12, 345, 2, 6, 7896]
print(Solution.findNumbers(s, a))

b = [555, 901, 482, 1771]
print(Solution.findNumbers(s, b))
