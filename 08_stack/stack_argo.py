#判断括号是否合适 https://leetcode-cn.com/problems/valid-parentheses/submissions/
#括号生成   https://leetcode-cn.com/problems/generate-parentheses/
#目前 这个难度比较大 暂时不做 等复习完后面 再回来做
class Solution:
    def isValid(self, s: str) -> bool:
        #这个是我的实现 下面是别人的实现 对比下 就知道自己写的不够优雅
        hash_map = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i not in hash_map:
                stack.append(i)
            elif stack!=[] and hash_map[i] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map_dict = {"}":"{", "]":"[", ")":"("}
        for item in s:
            if item not in map_dict:
                stack.append(item)
            elif not stack or map_dict[item] != stack.pop():
                return False
        return not stack 

    def isValid2(self, s):
        while '{}' in s or "()" in s or "[]" in s:
            s = s.replace("{}", "").replace("()","").replace("[]","")
        return len(s) == 0
