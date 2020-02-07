# TIE-02100 Johdatus ohjelmointiin
# TIE-02100 Introduction to programming
# Template song b, Old MacDonald
def print_verse(x,y):
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a",x)
    print("E-I-E-I-O")
    print("With a", y, y, "here")
    print("And a",y,y,"there")
    print("Here a ",y,","," there a ",y,sep='')
    print("Everywhere a",y,y)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()

def main():

    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

main()
