def fibonacci(n):
    """
    Return `n`th Fibonacci number for a positive value of `n`.
    The value of the number at position n in the Fibonacci equence is determined by:
        F[n] = F[n - 1] + F[n - 2]
        where: F[0] = 0 and F[1] = 1
    """
    prev = 0
    current = 1
    
    if 0 <= n <= 1: return n

    count = 1

    while count < n:
        next = current + prev
        prev = current
        current = next
        count += 1
    
    return current



print(", ".join(str(fibonacci(i)) for i in range(1, 11)))

print(fibonacci(6))