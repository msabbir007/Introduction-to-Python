Entered_number=[]
grt_than_zro=[]
print("Give 5 numbers:")
for i in range(5):
    a=int(input("Next number: "))
    Entered_number.append(a)
    if a>0:
        grt_than_zro.append(a)
print("The numbers you entered that were greater than zero were: ")
print(*grt_than_zro, sep='\n')




