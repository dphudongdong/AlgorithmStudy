"""
给定两个字符串 order 和 s 。order 的所有单词都是 唯一 的，并且以前按照一些自定义的顺序排序。
对 s 的字符进行置换，使其与排序的 order 相匹配。更具体地说，如果在 order 中的字符 x 出现字符 y 之前，那么在排列后的字符串中， x 也应该出现在 y 之前。
返回 满足这个性质的 s 的任意排列 。
"""
import collections
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
            方式1：给每个字符设置排列优先级 对于order里面的给予较低的值，在排序时排在前面
        '''
        dic = collections.defaultdict(int)
        # 建立defaultdict 若key不在dic中返回0
        lens = len(order)
        for i,st in enumerate(order): 
            dic[st]= i-lens
        print(dic)
        # 将order中的每个字符加入dic，对应的值为其下标
        return "".join(sorted(list(s),key=lambda x:dic[x]))
        # 将s按dic中的值排序，若不在dic中，顺序随意w
    def customSortString1(self, order, s):
        '''
            统计下s中每个字符的数量
            对在order中的每个字符 如果在s中则写入list中，将对应字符的count变成0
            之后对不在order中的字符 在依次写入list
            之后组合即可
        '''
        count = collections.Counter(s)
        print(count)
        ans = []

        for c in order:
            ans.append(c * count[c])
            count[c] = 0
        print(count)
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)


if __name__ == '__main__':
    a =Solution()
    print(a.customSortString("cba","abcd"))
    print(a.customSortString1("cba","abcd"))