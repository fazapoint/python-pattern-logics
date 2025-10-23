class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split(" ")
        return(len(last_word[-1]))

obj = Solution()
print(obj.lengthOfLastWord("Hello Worldd"))
