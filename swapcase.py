# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):

    newList[0],newList[-1] = newList[-1],newList[0]

    return newList