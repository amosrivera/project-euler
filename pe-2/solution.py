t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    new = 0
    total = 10
    prev = 2
    current = 8

    if n < 8:
        total = 2

    if n < 2:
        total = 0

    while True:
        new = (4 * current) + prev

        if (new > n):
            break

        total   += new
        prev    = current 
        current = new
    
    print (total)
