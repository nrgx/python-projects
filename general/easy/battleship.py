"""
A Battleship game.
1. Create 2 matrices with DxD dimension filled in with M markings.
First matrix is for user, the second one is for PC.
2. Randomly set up 5 ships so that they could fit in to each matrix,
e.g. ships MUST NOT:
 - overlap each other;
 - placed diagonally;
 - hang off the grid.
3. Show user 2 matrices. First matrix - PC's matrix, must be escaped by OVERLAY var.
Second matrix is user's matrix. Show it normally with 0's and ships.
If ship's cell of any matrix is hit then update the output with mark 'X' on this cell.
4. Provide for an user an input where he must enter
coordinates by this notation `0..D-1;0..D-1`, like `0;9`, `5;3`, `8;7`, etc.
5. For PC's turn choose random values from the same ranges `0..D-1;0..D-1`,
check cell's value:
if it's '0' -> pass turn
else mark it with 'X'
"""
import random
import itertools as it


OVERLAY = "≋"
CARRIER = ['1'] * 5
BATTLESHIP = ['2'] * 4
CRUISER = ['3'] * 3
SUBMARINE = ['4'] * 3
DESTROYER = ['5'] * 2
SHIPS = [
    CARRIER,
    BATTLESHIP,
    CRUISER,
    SUBMARINE,
    DESTROYER,
]
M = '0'
# Dimension
D = 9
# Occasionally this notation `[['0' * D]] * D`
# (where D is any integer) creates just one list (the inner ['0' * D] part)
# and then makes a reference to that list for every
# outer ([...] * D part) multiplication by D


def generate_table(mark: str, repeat: int):
    """Generate table
    Generates a table with dimension
    `repeat X repeat` and fills in whatever mark is passed
    :param mark: whatever single character string
    :param repeat: the dimension for table
    :return: list of lists
    """
    return [[mark for _ in range(repeat)] for _ in range(repeat)]


# User's table
TABLE1 = generate_table(mark=M, repeat=D)
# PC's table
TABLE2 = generate_table(mark=M, repeat=D)
# Positions: V for vertical and H for horizontal
V = "V"
H = "H"


def generate_matrix(mark: str, table: list[list]):
    # Need to set up all battleships
    counter = 0
    while True:
        ship = SHIPS[counter]
        length = len(ship)
        pos = random.choice([V, H])
        if pos == H:
            # Setting up ship in horizontal position
            random_row = random.randint(0, len(table) - 1)
            if all(x == mark for x in table[random_row]):
                # if row is empty, e.g. filled only with '0',
                # get random index of this row,
                # from this index set up a ship in a row
                random_row_index = random.randint(0, D - length - 1)
                table[random_row][random_row_index: length + random_row_index] = ship
            else:
                # if the row contains something other than '0'
                # then check if there is enough room to set up another ship
                # btw `groupby` from itertools does a good job in grouping items.
                # I was thinking about grouping too long
                groups = []
                for _, group in it.groupby(table[random_row], key=lambda x: x == M):
                    groups.append(list(group))
                for group in groups:
                    if all(item == M for item in group) and len(group) == length:
                        groups[groups.index(group)] = ship
                        break
                table[random_row] = [item for g in groups for item in g]
        else:
            # Well this one is tough.
            # Check the matrix vertically by columns
            random_col = random.randint(0, len(table) - 1)
            column = [row[random_col] for row in table]
            if all(x == mark for x in column):
                random_col_index = random.randint(0, D - length - 1)
                column
        counter += 1
        if counter == 5:
            break
