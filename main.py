board = [
    [6, 0, 1, 5, 9, 0, 8, 0, 7],
    [2, 0, 5, 0, 1, 0, 0, 0, 0],
    [0, 4, 0, 6, 0, 0, 0, 3, 0],
    [0, 2, 0, 0, 7, 5, 0, 0, 6],
    [7, 0, 4, 0, 6, 9, 0, 1, 8],
    [1, 6, 9, 0, 4, 8, 0, 0, 0],
    [0, 0, 7, 4, 5, 1, 0, 6, 0],
    [0, 0, 0, 9, 0, 2, 3, 0, 0],
    [4, 0, 0, 0, 0, 6, 0, 0, 5]

]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                if bo[i][j] == 0:
                    print(" ")
                else:
                    print(bo[i][j])
            else:
                if bo[i][j] == 0:
                    print("  ", end="")
                else:
                    print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return j, i  # returns the x, y coordinate of the blank spot on the board ( top left being 0,0 )


print_board(board)
