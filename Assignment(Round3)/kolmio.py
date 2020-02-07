# Johdatus ohjelmointiin
# Introduction to programming
# Area
def area(a,b,c):
    s=(a+b+c)/2
    import math
    tem=(s-a)*(s-b)*(s-c)
    result= math.sqrt(s*tem)
    return result


def main():
    line_a = float(input("Enter the length of the first side: "))
    line_b = float(input("Enter the length of the second side: "))
    line_c= float(input("Enter the length of the third side: "))
    print("The triangle's area is ","{0:.1f}".format(area(line_a,line_b,line_c)))
    

main()
