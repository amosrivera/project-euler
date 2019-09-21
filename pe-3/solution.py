from math import sqrt

def get_max_factorial(number):
    candidate = 2
    reduced = number
    limit   = sqrt(reduced)
    max_f = 0

    while (reduced > 1):
        if candidate > limit: 
            # number is or has been reduced to a prime
            max_f = reduced
            break

        if (reduced % candidate == 0):            
            max_f = candidate
            reduced = reduced // candidate
            limit = sqrt(reduced)
        else:
            candidate += 1

    if not max_f:
        max_f = number

    return max_f

cases = int(input().strip())
for case in range(cases):
    number = int(input().strip())
    print(get_max_factorial(number))
