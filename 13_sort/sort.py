"""
    桶排序 https://www.jianshu.com/p/b445e94a9a21
    计数排序 https://segmentfault.com/a/1190000022744724
    https://mp.weixin.qq.com/s/KU-AUGOnLeRtE_hivl2uSA
    基数排序 https://segmentfault.com/a/1190000022759528
    
"""
from typing import List

def bucket_sort(arr:List[int]):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶数组
    count_list = [[] for _ in range(max_num- min_num+ 1)]
    print (len(count_list))
    # 向桶数组填数
    for i in arr:
        count_list[i-min_num].append(i)
    arr.clear()
    print(count_list)
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            arr.append(j)

def count_sort(arr):
    """
        此计数排序是严格按照最后遍历从后往前来的
        其实在算完count之后 不考虑算法稳定性的话 直接打印就OK了 也就是注释的部分
    """
    max = min = 0
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    count = [0] * (max-min+1)

    for index in arr:
        count[index-min]+=1

    # index=0
    # for a in range(max-min+1):
    #     for c in range(count[a]):
    #         arr[index]=a+min
    #         index+=1
    for i in range(1,max-min+1):
        count[i] = count[i]+count[i-1]
    new_arr  = ["" for _ in arr] 
    for i in range(len(arr)-1,-1,-1):
        index = count[arr[i]-min]-1
        new_arr[index] = arr[i]
        count[arr[i]-min]-=1
    return new_arr
   


def radix_sort(arr:List[int]):
    '''
        基数排序 从个位数开始不断进行排序
        因为只有可能是0到9 只需要10个桶就行
        然后一次把对应位置相同的放一起
        
    '''
    n = len(str(max(arr)))  # 记录最大值的位数
    for k in range(n):#n轮排序
        # 每一轮生成10个列表
        bucket_list=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
        print(bucket_list)
        for i in arr:
            # 按第k位放入到桶中
            bucket_list[i//(10**k)%10].append(i)
        # 按当前桶的顺序重排列表
        print(bucket_list)
        arr=[j for i in bucket_list for j in i]
        print(arr)
    return arr


if __name__ == '__main__':
    import random
    random.seed(54)
    arr = [random.randint(0,100) for _ in range(10)]
    print("原始数据：", arr)
    # bucket_sort(arr)
    arr = count_sort(arr)
    # arr = radix_sort(arr)
    print("排序结果：", arr)