"""
    数组中的第K个最大元素
"""
#https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
from typing import List
#方法1 如果将数据从小到大排 如果len=n 第K大对应的index就是n-k 所以我们就是找到对应的index即可
#使用快排将数组分成3部分A[0...p-1]、A[p]、A[p+1...n-1]。 如果index==P返回即可
#如果index大于p，则需要在递归下A[p+1,n-1],反之亦然
#我们需要对大小为 n 的数组执行分区操作，需要遍历 n 个元素。
# 第二次分区查找，我们只需要对大小为 n/2 的数组执行分区操作，需要遍历 n/2 个元素。
# 依次类推，分区遍历元素的个数分别为、n/2、n/4、n/8、n/16.……直到区间缩小为 1。
# 如果我们把每次分区遍历的元素个数加起来，就是：n+n/2+n/4+n/8+...+1
# 。这是一个等比数列求和，最后的和等于 2n-1。所以，上述解决思路的时间复杂度就为 O(n)。

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)

    def quickSelect(self, nums, low, high, index):
        m = self._partition(nums, low, high)
        if m == index:
            return nums[m]
        elif m<index:
            return self.quickSelect(nums, m + 1, high, index)
        else:
            return self.quickSelect(nums, low, m-1, index)

    def _partition(self, nums, low, high):
        pivot,j = nums[low], low
        for i in range(low+1,high+1):
            if nums[i] < pivot:
                j+=1
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], pivot
        return j
        
if __name__ == "__main__":
    s =Solution()
    nums = [3,2,1,5,6,4]
    k =2
    print(s.findKthLargest(nums,k))