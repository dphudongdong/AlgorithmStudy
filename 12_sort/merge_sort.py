'''
    归并排序
'''
#递归实现
#非递归实现  https://www.jianshu.com/p/3f27384387c1
def merge_sort(seq):
    if len(seq) <=1:
        return seq
    mid = len(seq) //2 # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    result +=left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    seq = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    seq = merge_sort(seq)
    print(seq)





