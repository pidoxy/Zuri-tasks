# first input: number 1
num1 = float(input("Enter first number:"))

# list of operators
print("Select operator.")
print("+. Add")
print("-. Subtract")
print("*. Multiply")
print("/. Divide")
print("%. Modulus -- show remainder")

# choose operator function
op = input("Enter operator:")

# second input: number 2
num2 = float(input("Enter second number:"))

# conditional statements
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1- num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1 * num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator")
 #Pidoxy is a sure guy

