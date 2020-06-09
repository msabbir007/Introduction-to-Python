# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: viesti, program code template









def read_message():
    text=''
    a=(input())
    while a!='':
        text+=a
        text+='\n'
        a = (input())
    return text

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for k in msg:
        print(''.join(k[:]).upper(),end='')
main()
