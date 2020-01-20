a=int(input("How many numbers would you like to have? "))
for x in range(1,a+1):

    if x%3==0 and x%7==0:
        print("zipboing")

    else:
        if x % 3 == 0:
            print("zip")
        elif x % 7 == 0:
            print("boing")
        else:
            print(x)