'''
Data Structure in Python
Hanyu in 2018
Last modified 3/5/2018
'''
import math

def binarySearch(array,item):
    #简单的二分查找法,必须经过排序的数组
    low = 0
    high = len(array)-1
    while (low <= high):
        mid = int((low+high)/2)
        if (item < array[mid]):
            high = mid - 1
        elif (item > array[mid]):
            low = mid + 1
        else:return mid
    return None

def mySelSort(array):
    #选择排序,自己写的版本,时间复杂度O(n**2),从大到小排序
    arrayNew = array[:]
    # 注意在复制数组时,仅写数组名表示指针标识符一样,一改则全改
    # 所以必须加[:]或(:),这样表示数组的复制
    n = len(array)
    for j in range(0,n-1):
        maxValue = array[0]
        maxIndex = 0
        for i in range(0,len(array)):
            if array[i] > maxValue:
                maxValue = array[i]
                maxIndex = i
        del array[maxIndex]
        arrayNew[j] = maxValue
    return arrayNew

def selectionSort(arr):
    # 书上写的代码,从小到大排序
    def findSmallest(arr1):
        # 找到一个最小的数,并输出其索引index
        smallest = arr[0]
        smallest_index = 0
        for i in range(1,len(arr1)):
            if arr1[i] < smallest:
                smallest = arr1[i]
                smallest_index = i
        return smallest_index

    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# 简单二分查找的测试程序
my_list = [1,3,5,7,9]
print(binarySearch(my_list,3)) #>=1
a = (2+3)/2
print(a) # pyhton3 不会自动转换数据类型,这里结果是2.5
b = 10**6/3600/24
print(b)
c = math.log(10**9) / math.log(2)
print(c)
# 简单二分查找的测试程序

# 自己写的选择排序的测试程序
my_list2 = [3,2.4,3.1415927,22,55,1e5,-20.5]
my_list2_sort = mySelSort(my_list2[:])
my_list2_sort2 = selectionSort(my_list2)
print(my_list2,my_list2_sort,my_list2_sort2)
#自己写的选择排序的测试程序

