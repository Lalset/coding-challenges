# HackerRank Mode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        normal = x
        reverse = 0

        while x > 0:
            last_number = x % 10
            reverse = reverse * 10 + last_number
            x //= 10

        return normal == reverse


#Local Mode
# if __name__ == "__main__":
#     solution = Solution()
#     x = int(input("Digite um número: "))
#     print(solution.isPalindrome(x))

