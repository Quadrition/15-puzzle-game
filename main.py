import table
from datetime import datetime


accuracy = 25


def main():

    # Chose state here
    board = ((7, 3, 5, 10), (11, 0, 6, 9), (12, 15, 2, 14), (4, 1, 8, 13))

    # Chose accuracy (more accuracy, more time but less moves)
    # Recommended accuracy 25%
    try:
        global accuracy
        accuracy = int(raw_input('Input accuracy: '))
        if not 0 <= accuracy <= 100:
            raise ValueError
    except ValueError:
        print 'Invalid accuracy'
        return

    # Count time
    start_time = datetime.now()
    moves, path = solve(board)
    end_time = datetime.now()

    # Print results
    print 'Solved in', end_time - start_time
    print 'Number of moves:', moves

    # Prints path
    print '\nPath:\n'
    real_path = table.get_path(board, path)
    for board in real_path:
        print table.get_table_string(board)


def solve(board):
    path = {}
    number_of_moves = -1

    current = {board}

    while True:
        number_of_moves += 1
        next_moves = set()
        for element in current:
            if table.is_solved(element):
                return number_of_moves, path
            for next_move in table.find_next_moves(element):
                next_moves.add(next_move)
                if hash(next_move) not in path:
                    path[hash(next_move)] = element

        current = set(next_moves)

        array = sorted(current, key=table.heuristic)
        array = array[:accuracy * 10]

        current = set(array)


if __name__ == '__main__':
    main()
