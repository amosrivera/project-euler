t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    total = (
            3   * (((n-1)//3)  *    (((n-1)//3) +1))//2
        +   5   * (((n-1)//5)  *    (((n-1)//5) +1))//2
        -   15  * (((n-1)//15) *    (((n-1)//15)+1))//2
    )

    print(total)      