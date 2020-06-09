def reverse_name(name):
    tem=''
    t = name.find(',')
    if t!=-1:
        tem1 = (name[t + 1:]).strip()
        tem2 = (name[0:t]).strip()
        if len(tem1)==0:
            return tem2
        elif len(tem2)==0:
            return tem1
        elif len(tem1)==0 and len(tem2)==0:
            return tem
        else:
            return tem1+' '+tem2

    elif len(name)== 0:
        return tem
    else:
        return name[:].strip()
