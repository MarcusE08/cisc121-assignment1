# marcus eagle, 20606610

def solution(A): # define a function that takes an array and assigns it to A

    arrayLen = len(A) # assign a variable to the length of A

    for number in range(1, arrayLen + 2): # loop through every number in the array from 1 to arrayLen + 1

        if number not in A: # if the number is not in A,
            return number   # return it