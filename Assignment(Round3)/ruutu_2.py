# Johdatus ohjelmointiin
# Print a box with input checking
def print_box(a,b,c):
    for i in range(0, b):
        for j in range(0, a):
            print(c, end="")
        print()

def read_input(x):
    y = int(input(x))

    while True:

        if y<0:
            y = int(input(x))
        elif y==0:
            y = int(input(x))
        else:
            return y


def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print_box(width, height, mark)

main()
