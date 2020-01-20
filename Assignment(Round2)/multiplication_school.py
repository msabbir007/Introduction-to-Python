a=int(input("Choose a number: "))
for x in range(1,100000):
    b=a*x;
    print(x, '*', a,'=',b)
    if b>100:
        break
