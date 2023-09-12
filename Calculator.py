a = int(input("Enter first no.:"))
b = int(input("Enter second no.:"))
print("Enter + for addition")          #menu driven program or calculator
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")
choice = input("Enter symbol:")
if choice=='+':
    print(a+b)
elif choice=='-':
    print(a-b)
elif choice=='*':
    print(a*b)
elif choice=='/':
    print(a/b)
else:
    print("Invalid choice")
    
    
