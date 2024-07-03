

num = int(input("Enter your number: "))  

if num == 0:
    print("Zero")
else:
    sum = 0  # Initialize sum variable
    while num > 0:  # Use a while loop to iterate while num is greater than 0
        sum += num  # Add num to sum
        num -= 1  # Decrease num by 1 in each iteration

    print(f"The sum of numbers from {num} to 1 is: {sum}")
