"""
 Min Operations
"""

def minOperate(n: int)-> int:
    """
    Function to implement the min Operation algorithm
    """
    if n == 1:
        return 0
    operation: int = 0
    divisor: int = 2
    i = 0
    while i < n:
        if n % divisor == 0:
            n //= divisor
            operation += divisor
            i += 1
        else:
            divisor += 1

    return operation