
a=str(input("Answer Y or N: "))

if a=='Y' or a=='N':
    print('You answered ', a)

elif a== 'y' or a=='n':
    print('You answered ', a)

else:
    while a!='Y' or a!='N' or a!= 'y' or a!='n':
        print('Incorrect entry.')
        a = str(input("Please retry: "))
        if a=='Y' or a=='N' or a== 'y' or a=='n':

            print('You answered ',a)
            break


