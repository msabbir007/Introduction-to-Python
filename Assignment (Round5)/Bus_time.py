
def main():
    # define the default bus timing
    busschedule=[630,1015,1415,1620,1720,2000]
    #User define start time
    time_togo=int(input("Enter the time (as an integer): "))
    for i in range(len(busschedule)):
        if busschedule[i]>=time_togo:
            index=i
            break
        else:
            index=0
    print("The next buses leave: ")
    #Run for loop for next 3 bus time
    for j in range(index, index+3):
        # using remainder(%) to execute initial element of the list(busschedule)
        print(busschedule[j%len(busschedule)] )

main()