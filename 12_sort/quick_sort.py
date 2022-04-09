"""
    快排
    https://blog.csdn.net/razor87/article/details/71155518
    https://www.jianshu.com/p/2b2f1f79984e
"""
def quick_sort(seq):
    _quick_sort_between(seq, 0, len(seq)-1)

def _quick_sort_between(seq, low, high):
    '''
        这个排序算法 主要是选择第一个数作为pivot，然后往后遍历，对于小于当前pivot的
        j+1，然后再把这个值与j兑换。最后再把pivot与j兑换
        因为我们主要是看币pivot小的值有多少 只要比他小就在左边(假设有n个) 而最后pivot的值就会在第n+1的位置
        对应的下标也就是n
        这里很精妙 就是比pivot小的值从1开始放，之后累加 就把小于pivot的值都拍好了 而pivot最后再换一下就OK了
    '''
    if low < high:
        m = _partition(seq, low, high)  # a[m] is in final position
        _quick_sort_between(seq, low, m - 1)
        _quick_sort_between(seq, m + 1, high)


def _partition(seq, low, high):
    pivot, j = seq[low], low
    for i in range(low+1, high+1):
        if seq[i] <pivot:
            j+=1
            seq[i], seq[j] = seq[j], seq[i]
    seq[low], seq[j] = seq[j],pivot
    return j

if __name__ == "__main__":
    seq = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    quick_sort(seq)
    print(seq)

