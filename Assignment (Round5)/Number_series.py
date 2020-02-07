#Creat empty list to put all even number
empty_list=[]
for i in range(101):
    if i%2==0:
        print(i)
        empty_list.append(i)
#Reversing the even number list
Reverse_even_number=(empty_list[::-1])
for j in range(len(Reverse_even_number)):
    print(Reverse_even_number[j])