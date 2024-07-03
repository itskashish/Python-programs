num1 = int(input("Enter num1: "))
fun = input("Select operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")
num2 = int(input("Enter num2: "))

if fun == "1":
    print(f"{num1} + {num2} = {num1 + num2}")
elif fun == "2":
    print(f"{num1} - {num2} = {num1 - num2}")
elif fun == "3":
    print(f"{num1} * {num2} = {num1 * num2}")
elif fun == "4":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is undefined.")
else:
    print("Invalid operation selected.")
