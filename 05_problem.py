""" 
***
**
*
"""

# def pattern(n):
#     for i in range(n,0,-1):
#         print("*"*i)


# n=int(input("enter the number: "))
# a=pattern(n)        




#using recursion
def pattern_01(n):
    if (n==0):
         return
    
    print("*"*n)
    pattern_01(n-1)


n=int(input("enter th enumber:"))
pattern_01(n)
