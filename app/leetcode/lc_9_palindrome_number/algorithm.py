class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        list = [_ for _ in num]
        list_reversed = list[::-1]
        num2 = ''.join([str(_i) for _i in list_reversed ])
        if num2 == num:
            return True
        else:
            return False

    numbers = []
    number_input = None

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        if self.number_input is None:
            self.number_input = x
        remainder = x % 10
        x = int((x - remainder) / 10)
        self.numbers.append(remainder)
        if x / 10 >= 0.1:
            return self.isPalindrome2(x)
        else:
            num = 0
            for (i, _) in enumerate(self.numbers):
                num += _ * (10 ** (len(self.numbers)-(i+1)))
            if self.number_input == num:
                return True
            return False

if __name__ == '__main__':
    print(Solution().isPalindrome2(0))





# isPalindrom(100001)
# print(numbers)
