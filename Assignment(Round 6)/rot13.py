# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ROT13, program code template


def encrypt(alphabet):
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # Implement encryption here

    if regular_chars.__contains__(alphabet) == True:
        return (encrypted_chars[regular_chars.index(alphabet)])
    else:
        f = alphabet.lower()
        if regular_chars.__contains__(f) == True:
            return (encrypted_chars[regular_chars.index(f)].upper())
        else:
            return (alphabet)

def row_encryption(row):
    new_row=''
    for i in row:
        new_row+=encrypt(i)
    return new_row



