def main():
    time=[]
    for i in range(5):
        print("Enter the time for performance", i + 1, end='')
        time.append(float(input(': ')))
    time_sequence=sorted(time)
    del time_sequence[0],time_sequence[len(time_sequence)-1]
    total_time=0
    for j in range(len(time_sequence)):
        total_time+=time_sequence[j]

    avg=total_time/len(time_sequence)
    print("The official competition score is", "{0:.2f}".format(avg),"seconds.")

main()
