def greater(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    

a=int(input("enter the vaue of a:"))
b=int(input("enter the vaue of b:"))
c=int(input("enter the vaue of c:"))
a=greater(a,b,c)
print(f"the greatest of all among these value is {a}")

