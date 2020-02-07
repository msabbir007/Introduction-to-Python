total=0
T_number=5
mes_array=[0]*T_number
for i in range(T_number):
    print("Enter the measurement result", i+ 1, end='')
    mes_array[i] = float(input(': '))
    if 6 <= mes_array[i] <= 8:
        for j in range(i ):
            if abs(mes_array[j] - mes_array[j + 1])>1:
                print("The conditions are not suitable for zebra fishes.")
            else:
                total = sum(mes_array)
    else:
        print("The conditions are not suitable for zebra fishes.")





