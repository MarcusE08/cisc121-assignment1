# by marcus eagle, 20606610

def solution(X, Y, D):

    jumpCount = 0 # initialize a jump count at 0
    curPos = X # initialize the current position at x

    while True: # loop until broken

        if curPos >= Y: # check if the current position is greater than or equal to Y
            break # if it is, break the while loop

                            # if the current position is lower than Y,
        curPos = curPos + D # add the jump distance to the current position
        jumpCount += 1      # and add a jump to the counter

    return jumpCount # return the jump count after the while loop is broken