a=2020;

for i in range(1,13):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        for j in range(1,32):
            print(j, '.', i, '.', sep="")
    elif i==4  or i==6 or i==9 or i==11:
        for j in range(1,31):
            print(j, '.', i, '.', sep="")
    else:
        for j in range(1, 29):
            print(j, '.', i,'.', sep="")