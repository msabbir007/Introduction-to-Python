def read_data(a):
    total = 0
    #dilear empty measrurment array for storing measurment i/p data
    meas_array = [0] * a
    for i in range(a):
        print("Enter the measurement result", i + 1, end='')
        meas_array[i] = float(input(': '))
        if 6 <= meas_array[i] <= 8:
            for j in range(i):
                if abs(meas_array[j] - meas_array[j + 1]) > 1:
                    print("The conditions are not suitable for zebra fishes.")
                    # Return 0 to stop further execution
                    return 0
                else:
                    #count the total value of all measurment
                    total = sum(meas_array)
        else:
            print("The conditions are not suitable for zebra fishes.")
            #Return 0 to stop further execution
            return 0
    #Return the average Ph value to the main function
    return (total / a)

def Ph_decission(g):
    if 6 <= g <= 8:
        print("Conditions are suitable for zebra fishes. The average pH is ", "{0:.2f}".format(g), ".", sep='')

def main():
    x = int(input("Enter the number of the measurements: "))
    if x <= 0:
        print("Error: the number must be expressed as a positive integer.")
    else:
        avg_Ph_level= read_data(x)
        Ph_decission(avg_Ph_level)
main()