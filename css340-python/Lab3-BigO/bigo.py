import timeit

def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return mid
    return None

def find1(list, val):
    for i in list:
        if i == val:
            return True
    return False

def find2(list, val):
    list2 = list[:]
    list2.sort()
    if binarySearch(list2, val) is not None:
        return True

def find3(list, val):
    isMember = False
    if val in list:
        isMember = True
    return isMember


# list has to be sorted!
def find4(list, val):
    if binarySearch(list, val) is not None:
        return True

# compute find1 time 
def find1_time(): 
    SETUP_CODE = ''' 
from __main__ import find1 
from random import randint
mylist = [x for x in range(46000)] 
value = randint(0, len(mylist))'''
      
    TEST_CODE = ''' 
find1(mylist, value) 
    '''
    t = timeit.Timer(setup = SETUP_CODE, 
                          stmt = TEST_CODE)
    duration = t.timeit(1000)
   
    print("Find1 Time: ", duration, " ms")

# compute find2 time 
def find2_time(): 
    SETUP_CODE = ''' 
from __main__ import find2 
from random import randint
mylist = [x for x in range(131072)] 
value = randint(0, len(mylist)) '''
      
    TEST_CODE = '''
find2(mylist, value) 
    '''
    t = timeit.Timer(setup = SETUP_CODE, 
                          stmt = TEST_CODE)
    duration = t.timeit(1000)
    
    print("Find2 Time: ", duration, " ms")

# compute find3 time 
def find3_time(): 
    SETUP_CODE = ''' 
from __main__ import find3 
from random import randint
mylist = [x for x in range(10000)] 
value = randint(0, len(mylist))'''
      
    TEST_CODE = ''' 
find3(mylist, value) 
    '''
    t = timeit.Timer(setup = SETUP_CODE, 
                          stmt = TEST_CODE)
    duration = t.timeit(1000)
   
    print("Find3 Time: ", duration, " ms")

# compute find4 time 
def find4_time(): 
    SETUP_CODE = ''' 
from __main__ import find4 
from random import randint
mylist = [x for x in range(10000)] 
value = randint(0, len(mylist))
mylist.sort()
'''
      
    TEST_CODE = '''
find4(mylist, value) 
    '''
    t = timeit.Timer(setup = SETUP_CODE, 
                          stmt = TEST_CODE)
    duration = t.timeit(1000)
   
    print("Find4 Time: ", duration, " ms")
  
if __name__ == "__main__": 
    #find1_time()
    find2_time()
    #find3_time()
    #find4_time()


#def main():
my_list20 = [1, 2, 3, 32, 87, 7, 9, 11, 66, 34, 67, 55]
my_list20.sort()
value20 = 17
if find4(my_list20, value20):
    print(str(my_list20) + " has " + str(value20))
else:
    print(str(my_list20) + " doesn't have " + str(value20))

