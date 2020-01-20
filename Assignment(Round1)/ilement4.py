a=int(input('How do you feel? (1-10)'))

if 0<a<2:
    print("A suitable smiley would be :'(")
elif 2<=a<4:
    print("A suitable smiley would be :-(")
elif 4<=a<8:
  print("A suitable smiley would be :-|")
elif 8<=a<=9:
    print("A suitable smiley would be :-)")
elif a==10:
    print("A suitable smiley would be :-D")
else:
    print("Bad input!")
