'''
    二分查找 递归法
'''
def bsearch_recursion(seq, target):
    return bsearch_internally(seq, 0, len(seq)-1, target)

def bsearch_internally(seq, low, high, target):
    if low >high:
        return -1
    mid = low +((high-low)>>1)
    # mid = low + (high - low) // 2
    if seq[mid] == target:
        return mid
    elif seq[mid] < target:
        return bsearch_internally(seq, mid+1, high, target)
    else:
        return bsearch_internally(seq, low, mid-1, target)


if __name__ == '__main__':
    seq = [0,1,2,3,4,5,6]
    print(bsearch_recursion(seq, 2))