def isprime(num : int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def  isperfect(num : int) -> bool:
    
    """
        Determine if a number is a perfect number.
        
        A perfect number is a positive integer that is equal to the sum of its 
        proper positive divisors (excluding the number itself).
        
        Args:
            num (int): The number to check.
        
        Returns:
            bool: True if the number is perfect, False otherwise.
    """
    if num < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

