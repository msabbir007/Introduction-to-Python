def input_to_list(x):
    empty_list=[]
    print("Enter",x,"numbers:")
    for i in range(x):
        empty_list.append(int(input()))

    return empty_list


def main():
    a=int(input("How many numbers do you want to process: "))
    list=input_to_list(a)

    b = int(input("Enter the number to be searched: "))
    count = 0
    for k in range(len( list)):
        if b ==  list[k]:
            count += 1
    if count == 0:
        print(b, "is not among the numbers you have entered.")
    else:
        print(b, "shows up", count, "times among the numbers you have entered.")

main()
