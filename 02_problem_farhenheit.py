def convertor(c):
    return c*(9/5)+32 

c=float(input("enter the temperature in celcius: "))
a=convertor(c)
# print("the temperature in farhenheit is ",round(a,2),"F")#round(a,2) 2 denotes upto 2 decimal place
print(f"the temperature in farhenheit is {a}F")