def convertor(inch):
    return inch*2.54


inch=int(input("enter the measurement in inches: "))
a=convertor(inch)
print(a,"centimeters")
print(f"the corresponding values in cm is{convertor(inch)}")