def are_all_members_same(l):

    #print(len(l))
    if len(l)==0:
        return True

    else:
        first_element = (l[0])
        count = 0
        for i in range(len(l)):
            if abs(first_element-l[i])==0:
                count+=1
        if count==len(l):
            return True
        else:
            return False

