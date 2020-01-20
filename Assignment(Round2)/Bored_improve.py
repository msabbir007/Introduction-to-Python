a=str(input("Bored? (y/n) "))

while True:
    if a=='n':

        a = str(input("Bored? (y/n) "))

    elif a== 'y':
        print('Well, let\'s stop this, then.')
        break
    else:
        print('Incorrect entry.')
        a = str(input("Please retry: "))
