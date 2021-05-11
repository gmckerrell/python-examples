#
# A Collatz sequence in mathematics can be defined as follows.
# Starting with any positive integer:
#   if n is even, the next number in the sequence is n / 2
#   if n is odd, the next number in the sequence is 3n + 1
#
# It is conjectured that every such sequence eventually reaches the number 1.
# Test this conjecture.
#
# Bonus: What input n <= 1000000 gives the longest sequence?

def getNextValue(n):
    """
    This function returns the next integer in a Collatz sequence
    
    n - the current number
    """
    if (n % 2):
        # odd number
        return int(3 * n + 1)
    else:
        # even number
        return int(n / 2)

def collatz(value):
    """
    This function returns a collatz sequence for a given number
   
    value - the number to evaluate
    """
    sequence = [value]
    n = value
    while(True):
        n = getNextValue(n)
        sequence.append(n)
        if n == 1:
            break
    return sequence

def getLargest(maxValue):
    """
    This function will return the largest sequence less than the given maximum.

    maxValue - the maximum value to test
    """
    largest = []
    for i in range(1, maxValue):
        result = collatz(i)
        if len(result) > len(largest):
            largest = result
    return largest

# test some values
for i in (10,78,231,1897):
    print(collatz(i))

# find largest sequence
largest = getLargest(10000)
print(f"LARGEST:  ({len(largest)} entries)\n{largest}")
