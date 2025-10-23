class Solution():
    def isPalindrome(self, x: int) -> bool:

        # must be positive numbers
        if x < 0:
            return False
        
        reversed_num = 0
        copy_x = x
        while copy_x > 0:
            reversed_num = (reversed_num * 10) + (copy_x % 10)
            copy_x //= 10
        
        return reversed_num == x
        
obj = Solution()
print(obj.isPalindrome(222))