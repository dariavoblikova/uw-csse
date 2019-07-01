import random
import sys
import sort


if __name__ == "__main__":
    sortType = sys.argv[1]
    numberOfInt = sys.argv[2]
    mylist = []
    for i in range(int(numberOfInt)):
        randNumber = random.randint(1, int(numberOfInt))
        mylist.append(randNumber)
    
    if len(sys.argv) == 4:
        printString = sys.argv[3]
        if printString == 'PRINT':
            print("List before sorting:\n", mylist)
        else:
            print('you can only input PRINT as the last argument')
    
    if sortType == 'BubbleSort':
        mySort = sort.BubbleSort(mylist)
    elif sortType == 'InsertionSort':
        mySort = sort.InsertionSort(mylist)
    elif sortType == 'MergeSort':
        mySort = sort.MergeSort(mylist)
    elif sortType == 'IterativeMergeSort':
        mySort = sort.IterativeMergeSort(mylist)
    elif sortType == 'QuickSort':
        mySort = sort.QuickSort(mylist, 0, len(mylist) - 1)
    elif sortType == 'ShellSort':
        mySort = sort.ShellSort(mylist)

    if len(sys.argv) == 4:
        if printString == 'PRINT' and sortType == 'BubbleSort' or sortType == 'InsertionSort' or sortType == 'MergeSort' or sortType == 'IterativeMergeSort' or sortType == 'QuickSort' or sortType == 'ShellSort':
            print("List after sorting:\n ", mylist)
        else:
            print("You need to input sort type correctly!")