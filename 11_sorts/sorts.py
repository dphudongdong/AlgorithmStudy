'''
    Bubble sort, insertion sort and selection sort
    冒泡排序、插入排序、选择排序
'''

def bubble_sort(origin_list):
    length = len(origin_list)
    if length <=1:
        return origin_list
    for i in range(length):
        swap = False
        for j in range(length-i-1):
            if origin_list[j] > origin_list[j+1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
                swap = True
        if not swap:
            break
    return origin_list

def insertion_sort(origin_list):
    length = len(origin_list)
    if length <=1:
        return origin_list
    for i in range(1, length):
        value = origin_list[i]
        j = i - 1
        while j >=0 and origin_list[j]>value:
            origin_list[j+1] = origin_list[j]
            j -= 1
        origin_list[j + 1] = value
    return origin_list

def selection_sort(origin_list):
    length = len(origin_list)
    if length <=1:
        return origin_list
    for i in range(length):
        min_index = i 
        min_value = origin_list[i]
        for j in range(i+1, length):
            if origin_list[j] < min_value:
                min_index = j
                min_value = origin_list[j]
        origin_list[i], origin_list[min_index] = origin_list[min_index], origin_list[i]
    return origin_list

if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    array = bubble_sort(array)
    print(array)
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    array = insertion_sort(array)
    print(array)
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    array = selection_sort(array)
    print(array)
    