def compare_floats(a,b,EPSILON):
    v=a-b
    if v<= EPSILON:
       return print("True")
    else:
       return print("False")

def main():
    EPSILON = 0.00001
    compare_floats(0.00000000000000000001,0.0000000000000000002,EPSILON)

main()