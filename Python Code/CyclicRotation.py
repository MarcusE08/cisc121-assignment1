# marcus eagle, 20606610

def solution(A, K): # define a function that takes an array and amount of rotations

    if not A: # if A doesn't exist, return A
        return A

    for _ in range(K): # start a loop that repeats K times

        lastVal = A.pop() # assign a variable to pop the last value of the array

        A.insert(0, lastVal) # insert lastVal at index 0

    return A # return the rotated array