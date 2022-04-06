#https://leetcode-cn.com/problems/XltzEq/
#判断是否是回文
# a=[1,2,3,4,5]
# [::-1] 顺序相反操作  [5, 4, 3, 2, 1]
# [3::-1] 从下标为3（从0开始）的元素开始翻转读取 [4, 3, 2, 1]
# re.sub(r'\s+', '-', text) 将text句子中的“ ”替换为“-”
import re
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if not s[left].lower() == s[right].lower():
                return False
            right -= 1 
            left += 1
        return True



    
