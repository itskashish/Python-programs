num1 = int(input("enter ur num1:"))
num2 = int(input("enter ur num2:"))

for i in range(num1,num2 + 1):
    if i > 1:
        for j in range(2,i):
            if i%2 == 0:
                break
        else:
            print(i)
