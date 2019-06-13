what = input ("+,-: ")
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

if what =="+":
    c=a+b
    print("Result: " +str(c))
elif what =="-":
    c=a-b
    print("Result: " +str(c))
else:
    print("Unknown error")
    
