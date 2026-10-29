# marcus eagle, 20606610

def solution(A): # create a function that takes an array and assigns it to A

    arrayLen = len(A) # assign a variable to the length of A

    seen = set() # create a set for numbers that have already been seen

    for number in A: # start a loop for every number in A

        if number < 1 or number > arrayLen: # if the number is less than 1 or greater than arrayLen,
                                            # then it's not a permutation,
            return 0                        # so return 0

        if number in seen: # if the number is in seen, then it is not a permutation,
            return 0       # so return 0

        seen.add(number) # add the number to seen

    return 1 # if it passes the checks, then it is a permutation, so return 1