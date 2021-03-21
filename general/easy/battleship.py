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
from random import randint, choice
from itertools import groupby


HIT = "X"
CARRIER = ["1"] * 5
BATTLESHIP = ["2"] * 4
CRUISER = ["3"] * 3
SUBMARINE = ["4"] * 3
DESTROYER = ["5"] * 2
SHIPS = [
    CARRIER,
    BATTLESHIP,
    CRUISER,
    SUBMARINE,
    DESTROYER,
]
M = "≋"
# Dimension
D = 9
# Occasionally this notation `[['0' * D]] * D`
# (where D is any integer) creates just one list (the inner ['0' * D] part)
# and then makes a reference to that list for every
# outer ([...] * D part) multiplication by D

# Positions: V for vertical and H for horizontal
V = "V"
H = "H"


def generate_table(mark: str, repeat: int):
    """Generate table
    Generates a table with dimension
    `repeat X repeat` and fills in whatever mark is passed
    :param mark: whatever single character string
    :param repeat: the dimension for table
    :return: list of lists
    """
    return [[mark for _ in range(repeat)] for _ in range(repeat)]


def generate_matrix(table: list[list]):
    # Need to set up all battleships
    counter = 0
    while True:
        ship = SHIPS[counter]
        # print(ship)
        ship_length = len(ship)
        pos = choice([V, H])
        if pos == H:
            # print(f"Horizontal position")
            # Setting up ship in horizontal position
            random_row = randint(0, D - 1)
            if all(x == M for x in table[random_row]):
                # if row is empty, e.g. filled only with '0',
                # get random index of this row,
                # from this index set up a ship in a row
                random_row_index = randint(0, D - ship_length)
                # print(f"Random row index: {random_row_index}")
                table[random_row][
                    random_row_index : ship_length + random_row_index
                ] = ship
                counter += 1
                # print(f"Filled empty row #{random_row}")
            else:
                # if the row contains something other than '0'
                # then check if there is enough room to set up another ship
                # btw `groupby` from itertools does a good job in grouping items.
                # I was thinking about grouping too long
                groups = [
                    list(group)
                    for _, group in groupby(table[random_row], key=lambda x: x == M)
                ]
                # print(f"Groups for semi-full row #{random_row}: {groups}")
                for group in groups:
                    if all(item == M for item in group) and len(group) >= ship_length:
                        if len(group) == ship_length:
                            replacement = ship
                        else:
                            random_index = randint(
                                0, len(group) - ship_length - 1
                            )
                            group[random_index : random_index + ship_length] = ship
                            replacement = group
                        groups[groups.index(group)] = replacement
                        break
                new_row = [item for g in groups for item in g]
                # print(f"New row: {new_row}")
                table[random_row] = new_row
                counter += 1
                # print(f"Filled semi-full row #{random_row}")
        else:
            # print(f"Vertical position")
            # Well this one is tough.
            # Check the matrix vertically by columns
            random_col = randint(0, D - 1)
            random_row = randint(0, D - ship_length)
            column = [row[random_col] for row in table]
            if all(x == M for x in column):
                # So, if column is free (e.g. does not contain parts of other ships)
                # then chose random row from which ship building starts.
                # Iterate over ship's parts with indices, add index of iteration to row,
                # and leave column as is.
                for index, part in enumerate(ship):
                    table[random_row + index][random_col] = part
                counter += 1
                # print(f"Filled empty column #{random_col}")
            else:
                # Also use grouping but with column.
                # Then rewrite column of the table.
                groups = [
                    list(group) for _, group in groupby(column, key=lambda x: x == M)
                ]
                # print(f"Groups for semi-full column #{random_col}: {groups}")
                for group in groups:
                    if all(item == M for item in group) and len(group) >= ship_length:
                        if len(group) == ship_length:
                            replacement = ship
                        else:
                            random_index = randint(
                                0, len(group) - ship_length - 1
                            )
                            group[random_index : random_index + ship_length] = ship
                            replacement = group
                        groups[groups.index(group)] = replacement
                        break
                new_column = [item for g in groups for item in g]
                # print(f"New column: {new_column}")
                # Set new column into table
                for index, row in enumerate(table):
                    row[random_col] = new_column[index]
                counter += 1
                # print(f"Filled semi-full column #{random_col}")
        if counter == len(SHIPS):
            break
        # print("*=" * 10)
    return table


def test():
    """Test
    Debugging function
    :return:
    """
    table = generate_table(M, D)
    matrix = generate_matrix(table)
    for row in matrix:
        print(row)


def display(matrix: list[list]):
    """ Display matrix
    Shows pretty styled matrix
    :param matrix:
    :return:
    """
    for row in matrix:
        print(f"{' '.join(row)}")


def all_ships_destroyed(matrix: list[list]):
    """All ships destroyed
    Checks matrix for ship presence.
    If all cells are filled up with mark (M) or holes (HIT),
    then game is over.

    :param matrix:
    :return:
    """
    for row in matrix:
        for col in row:
            if col not in [M, HIT]:
                return False
    return True


def start():
    # Player #1 is user
    player1 = generate_matrix(generate_table(M, D))
    # Player #2 is pc
    player2 = generate_matrix(generate_table(M, D))
    player2_copy = generate_table(M, D)
    user_turn = True
    end = D - 1
    border = D * 2 - 1
    while True:
        print()
        display(player2_copy)
        print(f"{'=' * border}")
        display(player1)
        if user_turn:
            x = input(f"Enter X (from 0 to {end})\n").strip()
            y = input(f"Enter Y (from 0 to {end})\n").strip()
            if not x.isdigit() or not y.isdigit():
                x = input(f"Enter a digit for X from 0 to {end}\n").strip()
                y = input(f"Enter a digit for Y from 0 to {end}\n").strip()
            x, y = int(x), int(y)
            if x >= D or x < 0 or y >= D or y < 0:
                x = input(f"Enter digit value for X from 0 to {end}\n").strip()
                y = input(f"Enter digit value for Y from 0 to {end}\n").strip()
            if player2[x][y] != M:
                player2[x][y] = HIT
                player2_copy[x][y] = HIT
                # Check if all pc's ships destroyed
                if all_ships_destroyed(player2):
                    print("Congratulations, Admiral! You've destroyed all enemy ships!")
                    break
            user_turn = False
        else:
            # pc's turn
            x = randint(0, D - 1)
            y = randint(0, D - 1)
            if player1[x][y] != M:
                player1[x][y] = HIT
                # Check if all user's ships destroyed
                if all_ships_destroyed(player1):
                    print("We are defeated, Admiral! Our Armada was destroyed!")
                    break
            user_turn = True


if __name__ == '__main__':
    start()
