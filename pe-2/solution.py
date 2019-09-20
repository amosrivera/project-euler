t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    new = 0
    prev = 1
    current = 2
    total = 2

    while True:
        new = prev + current

        if (new > n):
            break

        if (not (new & 1)):
            total = total + new

        prev    = current 
        current = new
    
    print (total)