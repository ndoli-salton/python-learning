expression = input("Expression: ")

x,y,z = expression.split(" ")

if y == "+":
    print(f"{float(int(x) + int(z))}")
elif y == "-":
    print(f"{int(x) - int(z)}")
elif y == "*":
    print(f"{int(x) * int(z)}")
elif y == "/":
    if int(z) == 0:
        print("Cannot divide by zero")
    else:
        print(f"{int(x) / int(z)}")
else:
    print("Invalid operator")