# by marcus eagle, 20606610

def solution(A): # create a function that takes an array and assigns it to variable 'A'
    
    seen = set() # create a set

    for number in A: # look through every number in 'A'

        if number in seen: # if the number is in the 'seen' list, remove it as it has a match
            seen.remove(number)

        else: # if the number is not in the 'seen' list, add it
            seen.add(number)
        
    return seen.pop() # pop the 'seen' list and return the single remaining value