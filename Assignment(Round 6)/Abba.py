def  count_abbas(x):
    count = 0
    for i in range(len(x)):
        if x[i:i + 4] == "abba":
            count += 1
            i += 3
    return count

