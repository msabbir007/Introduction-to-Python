def is_the_list_in_order(l):

    if len(l) == 0:
        return True

    else:
        sort_l=sorted(l)
        if sort_l == l:

            return True
        else:

            return False
