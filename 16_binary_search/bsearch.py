from typing import List
def bsearch_left(nums: List[int], target: int) -> int:
    """
        Binary search of the index of the first element
        equal to a given target in the ascending sorted array.
        If not found, return -1.
        查找第一个值等于给定值的元素
    """
    low, high = 0, len(nums)-1
    while low<=high:
        mid = low+((high-low)>>1)
        if nums[mid] == target and nums[mid-1]!=target:
            return mid
        elif nums[mid] == target and nums[mid-1]==target:
            high =mid-1
        elif nums[mid] > target:
            high = mid -1
        else:
            low = mid +1
    return -1

def bsearch_left1(nums: List[int], target: int) -> int:
    """Binary search of the index of the first element
    equal to a given target in the ascending sorted array.
    If not found, return -1.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(nums) and nums[low] == target:
        return low
    else:
        return -1
if __name__ == '__main__':
    seq = [0,1,2,4,5]
    print(bsearch_left1(seq, 2))
        
        
