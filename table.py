from copy import deepcopy
dimension = 4
finish = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0))


# Finds blank space
def find_zero(board):
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == 0:
                return i, j


# Returns list of next moves
def find_next_moves(board):
    x_zero, y_zero = find_zero(board)
    moves = []
    board_list = [list(board[0]), list(board[1]), list(board[2]), list(board[3])]
    if y_zero != dimension - 1:
        list_left = deepcopy(board_list)
        list_left[x_zero][y_zero], list_left[x_zero][y_zero + 1] = \
            list_left[x_zero][y_zero + 1], list_left[x_zero][y_zero]
        tuple_left = tuple([tuple(list_left[0]), tuple(list_left[1]), tuple(list_left[2]), tuple(list_left[3])])
        moves.append(tuple_left)
    if y_zero != 0:
        list_right = deepcopy(board_list)
        list_right[x_zero][y_zero], list_right[x_zero][y_zero - 1] = \
            list_right[x_zero][y_zero - 1], list_right[x_zero][y_zero]
        tuple_right = tuple([tuple(list_right[0]), tuple(list_right[1]), tuple(list_right[2]), tuple(list_right[3])])
        moves.append(tuple_right)
    if x_zero != 0:
        list_down = deepcopy(board_list)
        list_down[x_zero - 1][y_zero], list_down[x_zero][y_zero] = \
            list_down[x_zero][y_zero], list_down[x_zero - 1][y_zero]
        tuple_down = tuple([tuple(list_down[0]), tuple(list_down[1]), tuple(list_down[2]), tuple(list_down[3])])
        moves.append(tuple_down)
    if x_zero != dimension - 1:
        list_up = deepcopy(board_list)
        list_up[x_zero + 1][y_zero], list_up[x_zero][y_zero] = \
            list_up[x_zero][y_zero], list_up[x_zero + 1][y_zero]
        tuple_up = tuple([tuple(list_up[0]), tuple(list_up[1]), tuple(list_up[2]), tuple(list_up[3])])
        moves.append(tuple_up)
    return moves


# Heuristic (manhattan distance and linear conflict)
def heuristic(board):
    score = 0
    for i in range(dimension):
        maximum = -1
        for j in range(dimension):
            value = board[i][j]
            if value != 0:
                score += abs(i - (value - 1) // dimension) + abs(j - (value - 1) % dimension)
                if ((value - 1) / dimension) == i:
                    if value > maximum:
                        maximum = value
                    else:
                        score += 2

    for i in range(dimension):
        maximum = -1
        for j in range(dimension):
            value = board[j][i]
            if value != 0 and ((value - 1) / dimension) == j:
                if value > maximum:
                    maximum = value
                else:
                    score += 2
    return score


# Check if puzzle is solved
def is_solved(board):
    return board == finish


# Returns path to the finish
def get_path(board, path):
    lead_path = [finish]

    current = finish
    while True:
        current = path[hash(current)]
        lead_path.append(current)
        if current == board:
            break

    lead_path = lead_path[::-1]
    return lead_path


# String representation of puzzle current state
def get_table_string(board):
    string = ''
    for row in board:
        for num in row:
            if len(str(num)) == 1:
                string += '   ' + str(num)
            elif len(str(num)) > 1:
                string += '  ' + str(num)
        string += '\n'
    return string
