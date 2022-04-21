'''
    二分查找非递归
'''
def bsearch(seq, target):
    low, high = 0, len(seq)-1
    while low<= high:
        # mid = low+((high-low)>>1)
        mid = low + (high - low) // 2
        if seq[mid] == target:
            return mid
        elif seq[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return -1


if __name__ == '__main__':
    seq = [0,1,2,3,4,5,6]
    print(bsearch(seq, 2))