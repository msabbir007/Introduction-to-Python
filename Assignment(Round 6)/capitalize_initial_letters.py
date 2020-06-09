def capitalize_initial_letters(name):
    t=name.split()
    m=''
    for i in t:
        if i!=t[len(t)-1]:
            for j in range(len(i)):
                if j==0:
                    m+=''.join(i[j]).upper()
                else:
                    m+=''.join(i[j]).lower()
            m+=' '

        else:
            for j in range(len(i)):
                if j==0:
                    m+=''.join(i[j]).upper()
                else:
                    m+=''.join(i[j]).lower()
    return m
