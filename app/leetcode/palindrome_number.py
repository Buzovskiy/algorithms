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