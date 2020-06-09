def create_an_acronym(name):
    t=name.split()
    m=''
    for i in t:
        m+=''.join(i[0]).upper()
    return m


