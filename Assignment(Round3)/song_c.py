# TIE-02100 Johdatus ohjelmointiin
# Koodipohja laulu c, Yogi Bear

def repeat_name(f,t):
    for i in range(0,t):
        print(f, ",", " ", f, " Bear", sep='')



def verse(x,y):
    print(x)
    print(y,",", " ", y, sep='')
    print(x)
    repeat_name(y,3)
    print(x)
    print(y,",", " ", y, " Bear", sep='')
    print()


def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

main()
