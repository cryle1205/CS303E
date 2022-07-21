# File: FindPrimeFactors.py
# Student: Crystal Le
# UT EID: CL44964
# Course Name: CS303E
# 
# Date Created: 10/28/2021
# Date Last Modified: 
# Description of Program: Checks if a number is prime and not less than 2 in order to
# perform prime factorization and output a list of prime factors. 
def isPrime(num):
    #checks if num is prime and returns if false or true
    if ( num < 2 or num % 2 == 0 ):
        return ( num == 2 )
    divisor = 3
    while ( divisor <= math.sqrt ( num )):
        if ( num % divisor == 0 ) :
            return False
        else :
            divisor += 2
    return True

while(True):
    #loops asking for an input integer from user unless it is 1 or less. Will return
    #prime factorization list
    num = int(input("Enter a positive integer (or 0 to stop): "))
    stored = 0
    stored +=num
    if num ==0:
        print("Goodbye!")
        break
    if num ==1:
        print("1 has no prime factorization.")
    elif num < 0:
        print("Negative integer entered.  Try again.")
    elif isPrime== True:
        print("The prime factorization of ", num, " is: [", num, "]", sep ="") 
    else:
        divisor = 2
        primeFactors = []
        while divisor <= num:
            if (num % divisor == 0):
                primeFactors.append(divisor)
                num/= divisor
            else:
                #only adds to divisor if num can no longer divide by 2, 3, 4...
                divisor += 1
        print("The prime factorization of", stored, "is:", primeFactors)
