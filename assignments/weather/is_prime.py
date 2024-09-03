import math

"""Checks if the number is prime.

Checks if the given number is an integer. Then checks if the number is greater than one. Finally checks
if the number is divisible by any integer up to its square root.

Input
num (integer)

Output
Bool: True if the number is prime, false otherwise. 
"""
def is_prime(num: int) -> bool:
    if num is None or not isinstance(num, int):
        return False
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True