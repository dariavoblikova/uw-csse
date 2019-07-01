import random
from random import randint
import timeit
import copy

def BubbleSort(inList):#n^2
    for i in range(len(inList)):
       for j in range(len(inList) - i - 1):
            if inList[j] > inList[j+1]:
                inList[j], inList[j+1] = inList[j+1], inList[j]

def InsertionSort(inList):#n^2
    for place in range(1, len(inList)):
        temp = inList[place]
        i = place
        while i > 0 and inList[i - 1] > temp:
            inList[i] = inList[i - 1]
            i = i - 1
        inList[i] = temp

def merge(inList, first, mid, last):
    size = last - first + 1
    tempList = [0] * size
    first1 = first
    last1 = mid
    first2 = mid + 1
    last2 = last
    index = 0
    while first1 <= last1 and first2 <= last2:
        if inList[first1] < inList[first2]:
            tempList[index] = inList[first1]
            first1 += 1
        else:
            tempList[index] = inList[first2]
            first2 += 1
        index += 1
    while first1 <= last1:
        tempList[index] = inList[first1]
        first1 += 1
        index += 1
    while first2 <= last2:
        tempList[index] = inList[first2]
        first2 += 1
        index += 1
    for index in range(size):
        inList[first] = tempList[index]
        first += 1

def mergeSortRec(inList, first, last):
    if first < last:
        mid = (first + last) // 2
        mergeSortRec(inList, first, mid)
        mergeSortRec(inList, mid + 1, last)
        merge(inList, first, mid, last)

def MergeSort(inList):#nlogn
    last = len(inList) - 1
    mergeSortRec(inList, 0, last)


def IterativeMerge(inList, tempList, first, mid, last):
    for i in range(first, last + 1):
        tempList[i] = inList[i]

    first1 = first
    first2 = mid + 1

    for i in range(first, last + 1):
        if first1 > mid:
            inList[i] = tempList[first2]
            first2 += 1

        elif first2 > last:
            inList[i] = tempList[first1]
            first1 += 1

        elif tempList[first2] < tempList[first1]:
            inList[i] = tempList[first2]
            first2 += 1

        else:
            inList[i] = tempList[first1]
            first1 += 1


def IterativeMergeSort(inList):#nlogn but better
    size = len(inList)
    tempList = [None] * size
    i = 1
    while i < size:
        j = 0
        while j < size:
            if (j + 2 * i - 1 >= size):
                IterativeMerge(inList, tempList, j, j + i - 1, size - 1)
            else:
                IterativeMerge(inList, tempList, j, j + i - 1, j + 2 * i - 1)
            j += 2 * i
        i += i
    return

def insertionSortPartialList(inList, first, last):
    for place in range(first + 1, last + 1):
        temp = inList[place]
        i = place
        while i > 0 and inList[i - 1] > temp:
            inList[i] = inList[i - 1]
            i = i - 1
        inList[i] = temp

def QuickSort(inList, first, last):#nlogn
    if last - first < 4:
        insertionSortPartialList(inList, first, last)#base case
        return
    #Choose the pivot using the sedgewick algorithm
    mid = (first + last) // 2
    if inList[first] > inList[last]:
        inList[first], inList[last] = inList[last], inList[first]
    if inList[first] > inList[mid]:
        inList[first], inList[mid] = inList[mid], inList[first]
    if inList[mid] > inList[last]:
        inList[mid], inList[last] = inList[last], inList[mid]
    pivot = inList[mid]
    inList[last - 1],inList[mid] = inList[mid],inList[last - 1]
    left = first + 1
    right = last - 2
    done = False
    while not done:
        while inList[left] < pivot:
            left += 1
        while inList[right] > pivot:
            right -= 1
        if right > left:
            inList[right], inList[left] = inList[left], inList[right] 
            left += 1
            right -= 1
        else:
            done = True
    inList[left], inList[last - 1] = inList[last - 1], inList[left]
    QuickSort(inList, first, left - 1)
    QuickSort(inList, left + 1, last)

def ShellSort(inList):#n^(3/2)
    size = len(inList)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = inList[i]
            j = i
            while j >= gap and temp < inList[j - gap]:
                inList[j] = inList[j - gap]
                j -= gap
            inList[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)


#def ListCreation(listSize):
#    mylist = []
#    mylist = [randint(0, listSize) for x in range(listSize)]

## compute list creation time
#def ListCreation_time(): 
#    SETUP_CODE = ''' 
#from __main__ import ListCreation
#from random import randint
#listSize = 100000
#'''
      
#    TEST_CODE = ''' 
#ListCreation(listSize)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("List Creation Time: ", duration, " ms")

##compute BubbleSort time
#def BubbleSort_time(): 
#    SETUP_CODE = ''' 
#from __main__ import BubbleSort
#from random import randint
#listSize = 15000
#mylist = []
#'''
      
#    TEST_CODE = ''' 
#mylist = [randint(0, listSize) for x in range(listSize)]
#BubbleSort(mylist)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("Bubble Sort Time: ", duration, " ms")


## compute InsertionSort time 
#def InsertionSort_time(): 
#    SETUP_CODE = ''' 
#from __main__ import InsertionSort
#from random import randint
#listSize = 15000
#mylist = []
#'''
      
#    TEST_CODE = ''' 
#mylist = [randint(0, listSize) for x in range(listSize)]
#InsertionSort(mylist)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("Insertion Sort Time: ", duration, " ms")
      
##compute MergeSort time 
#def MergeSort_time(): 
#    SETUP_CODE = ''' 
#from __main__ import MergeSort
#from random import randint
#listSize = 100000
#mylist = []
#'''
      
#    TEST_CODE = ''' 
#mylist = [randint(0, listSize) for x in range(listSize)]
#MergeSort(mylist)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("Merge Sort Time: ", duration, " ms")

##compute IterativeMergeSort time 
#def IterativeMergeSort_time(): 
#    SETUP_CODE = ''' 
#from __main__ import IterativeMergeSort
#from random import randint
#listSize = 100000
#mylist = []
#'''
      
#    TEST_CODE = ''' 
#mylist = [randint(0, listSize) for x in range(listSize)]
#IterativeMergeSort(mylist)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("IterativeMergeSort Time: ", duration, " ms")
      

##compute QuickSort time 
#def QuickSort_time(): 
#    SETUP_CODE = ''' 
#from __main__ import QuickSort
#from random import randint
#listSize = 100000
#mylist = []
#'''
      
#    TEST_CODE = ''' 
#mylist = [randint(0, listSize) for x in range(listSize)]
#QuickSort(mylist, 0, len(mylist) - 1)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("Quick Sort Time: ", duration, " ms")


## compute ShellSort time 
#def ShellSort_time(): 
#    SETUP_CODE = ''' 
#from __main__ import ShellSort
#from random import randint
#listSize = 100000
#mylist = []
#'''
      
#    TEST_CODE = ''' 
#mylist = [randint(0, listSize) for x in range(listSize)]
#ShellSort(mylist)
#    '''
#    t = timeit.Timer(setup = SETUP_CODE, stmt = TEST_CODE)
#    duration = t.timeit(5)

#    print("Shell Sort Time: ", duration, " ms")

#if __name__ == "__main__": 
#    BubbleSort_time()
#    InsertionSort_time()
#    MergeSort_time()
#    IterativeMergeSort_time()
#    QuickSort_time()
#    ShellSort_time()
#    ListCreation_time()