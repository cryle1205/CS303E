# File: ComparingLinearBinarySearch.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 11/03/2021
# Date Last Modified: 11/05/2021
# Description of Program: Performing Linear and Binary Searches on a list of values
# from [0:999]. Keys are randomly generated and the average number of probes are calculated.

import random
import math

###Linear Search###
def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    random.shuffle(lst)
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

###Binary Search###
def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

###Printing outcome###
###Linear Search Outcome###
print("Linear search:")
list1 = [x for x in range(1000)]
key = [x for x in range(1000)]
random_key = random.randint(key[0],key[-1])
tests = 10
total = 0
while(tests <= 100000): 
    for i in range(tests):
        probes= linearSearch(list1, 110) + 1 
        total += probes
    print("  Tests: ", format(tests, "<6d"), "   Average probes: " , (total/tests), sep= "")
    tests = tests * 10
    total = 0
    random_key = random.randint(key[0],key[-1])
###Binary Search Outcome###
list1.sort()
random_key = random.randint(key[0],key[-1])
total = 0
for i in range(1000):
    index,count = binarySearch(list1, random_key)
    total+=count
    random_key = random.randint(key[0],key[-1])
print("Binary search:")
print("  Average number of probes:", (total/1000))
print("  Differs from log2(1000) by:", math.log2(1000)- (total/1000))

