# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for task: ruutu
def print_box(a,b,c):
    for i in range(0, b):
        for j in range(0, a):
            print(c, end="")
        print()



def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark=input("Enter a print mark: ")

    print_box(width, height,mark)


main()
