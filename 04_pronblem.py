def sum(n):
    if (n==0):
        return 0
    return n+sum(n-1)


n=int(input ("enter the number till which you reqire sumation: "))
a=sum(n)
print(f"the sum of first {n} natural number is {a}")