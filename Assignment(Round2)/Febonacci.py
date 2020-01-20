i=int(input("How many Fibonacci numbers do you want? "))
a=0;
b=1;
if i<0:
    print("incorrect input")
else:
    for x in range(1,i+1):
        if x == 1:
            print(x, '.', b)
        else:
            c=a+b
            a=b
            b=c
            print(x, '.', c)


