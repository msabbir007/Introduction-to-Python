a=2014;
c = 3;
b=7;
for i in range(1,13):

    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        for j in range(c,32,7):
            print(j, '.', i, '.', sep="")
            c = 7-(31-j);
    elif i==4  or i==6 or i==9 or i==11:
        for j in range(c,31,7):
            print(j, '.', i, '.', sep="")
            c = 7 - (30 - j);
    else:
        for j in range(c, 29,7):
            print(j, '.', i,'.', sep="")
            c = 7 - (28 - j);