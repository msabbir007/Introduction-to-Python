Entered_number=[]
rev_ent_number=[]
print("Give 5 numbers:")
for i in range(5):
    a=int(input("Next number: "))
    Entered_number.append(a)

Entered_number.reverse()
print("The numbers you entered, in reverse order: ")
print(*Entered_number, sep='\n')