# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template

def main():

    # TODO: implement the datastructure for storing the board

    board=[['.','.','.'],['.','.','.'],['.','.','.']]

    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end='')
        print()


    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.

    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"

        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)
            if board[y][x] != ".":
                print("Error: a mark has already been placed on this square.")
                continue


            board[y][x]=mark
            print()


            # TODO: implement the turn of one player here
            turns += 1

            for i in range(len(board)):
                for j in range(len(board)):
                    print(board[i][j], end='')
                print()

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")

main()
