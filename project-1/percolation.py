from sys import setrecursionlimit
setrecursionlimit(10000000)
# We use the above function to set recurion limit above the defalut value, to allow higher dim matrices

from copy import deepcopy
# We use deepcopy function to copy the open_matrix in memory not only to assign new pointer to the same space in memory

def _percolation(open_matrix, full_matrix, x, y):
    '''
    Recursive funcrion which checks wheather there is an option to move through matrix
    '''
    dim = len(open_matrix)
    # First we check whether our indexes are in bounds
    if (x < 0) or (x >= dim):
        return

    if (y < 0) or (y >= dim):
        return

    # Then we check whether current point is open
    if open_matrix[x][y] == 2:
        return

    if full_matrix[x][y] == 1:
        return

    # Now we change the value to 1 to signalize that we already checked this point
    full_matrix[x][y] = 1

    # And at last we move in every direction
    _percolation(open_matrix, full_matrix, x+1, y  )  # MOVE DOWN
    _percolation(open_matrix, full_matrix, x  , y+1)  # MOVE RIGHT
    _percolation(open_matrix, full_matrix, x  , y-1)  # MOVE LEFT
    _percolation(open_matrix, full_matrix, x-1, y  )  # MOVE UP

def percolation(open_matrix):
    '''
    Function which checks wheather our system percolates and returns tuple with bool value and full_matrix if it percolates and only bool value it it doesn't

    Atributes:
    ----------

    open_matrix : 2D list with both dimensions being equal
    '''
    # First we create full_matrix
    full_matrix = deepcopy(open_matrix)
    dim = len(open_matrix)

    # Here we check fill up full_matrix with with postion we can move to from the first row
    for y in range(dim):
        _percolation(open_matrix, full_matrix, 0, y)

    # Here we check whether our system percolates by checking if we reached last row with operation above
    # We return tuple with bool value and filled matrix
    for y in range(dim):
        if full_matrix[dim-1][y] == 1:
            return (True, full_matrix)
    return (False, full_matrix)

if __name__ == '__main__':
    # This tests non percolating matrix
    not_percolating_matrix = [[2, 2, 2], [0, 0, 0], [2, 2, 2]]
    assert percolation(not_percolating_matrix) == (False, [[2, 2, 2], [0, 0, 0], [2, 2, 2]])
    
    # And this tests percolating matrix
    percolating_matrix = [[2, 0, 2], [0, 0, 0], [2, 0, 2]]
    assert percolation(percolating_matrix) == (True, [[2, 1, 2], [1, 1, 1], [2, 1, 2]])