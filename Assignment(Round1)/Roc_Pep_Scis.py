a=input('Player 1, enter your choice (R/P/S):')
b=input('Player 2, enter your choice (R/P/S):')
if a=='R' and b=='P':
    print('Player 2 won!')
elif a == 'P' and b == 'R':
    print('Player 1 won!')
elif a == 'S' and b == 'R':
    print('Player 2 won!')
elif a=='R' and b=='S':
    print('Player 1 won!')
elif a =='P' and b =='S':
    print('Player 2 won!')
elif a =='S' and b =='P':
    print('Player 1 won!')

else:
    print("It's a tie!")
