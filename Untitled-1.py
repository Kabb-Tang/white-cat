def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制需要比较的轮数
    for i in range(n):
        # 内层循环控制每轮比较的次数
        for j in range(0, n-i-1):
            # 如果前面的数比后面的大，则交换位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试代码
test_array = [64, 34, 25, 12, 22, 11, 90]
print("排序前的数组:", test_array)
sorted_array = bubble_sort(test_array)
print("排序后的数组:", sorted_array)