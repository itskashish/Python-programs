num1 = int(input("enter num1:"))


if num1 == 1:
    print("neither prime nor odd")
elif num1>1:
    for i in range(2,num1):
        if num1%i==0:
            print("not prime num")
            break
    else:
        print("prime")


