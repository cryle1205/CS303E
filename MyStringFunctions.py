# File: MyStringFunctions.py
# Student: Crystal Le   
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created:10/23/2021
# Date Last Modified: 10/25/2021
# Description of Program: Functions of that perform different string methods
# without using any Python inbuilt functions. 

def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    pass
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in str:
        if i == ch:
            count+=1
    return count 
    
def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2
    

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if len(str) == 0:
        print("Empty string: no min value")
        return None
    else:
        lowest = min(str)
        return lowest

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i > len(str):
        print("Invalid index")
        return None
    else:
        newString   =  str[:i] + ch + str[i:]
        return newString
    
def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if i >= len(str):
        print("Invalid index")
        return str, None
    else:
        newString = str[:i] + str[i+1:]
        return newString, str[i]

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    i = 0
    for i in range(len(str)):
        if ch not in str:
            return -1
        elif ch in str[i]:
            return i
        else:
            i+=1
        
def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    i = 0
    a = 0
    for i in range(len(str)):
        if ch not in str:
            return -1
        elif ch in str[i]:
            a = i 
        else:
            i+=1
    return a 

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    for i in range(len(str)):
        if ch not in str:
            return str
        elif ch in str[i]:
            return str[:i] + str[i+1:]
        else:
            i+=1
        

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    i = 0
    s = ""
    for i in range(len(str)):
        if ch not in str:
            return str
        elif ch in str:
            if str[i] != ch:
                s += str[i]
        else:
            i+=1
    return s

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    newString = str[::-1]
    return newString
    
