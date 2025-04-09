from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
print("Hello!")
a=int(input("Enter 1st no.: "))
b=int(input("Enter 2nd no.: "))
c=input("""Here are some operations that you can perform in this:
1. Press 1 for addition 
2. Press 2 for subtraction 
3. Press 3 for multiplication
4. Press 4 for division
""")
if c=="1":
    print(add(a,b))
elif c=="2":
    print(subtract(a,b))
elif c=="3":
    print(multiply(a,b))
elif c=="4":
    print(divide(a,b))