from random import choices

def creat_matrix(n, p):
    '''
    Function which creates n×n matrix filled with twos with probability p and zeros with probability 1-p
    Atributes:
    ---------
    n : int
        dimension of matrix

    p : float
        probability of 1 occuring in matrix
    '''
    # 0 = open
    # 2 = closed
    # I've chosen to use 2 instead of 1 due to cosmetic reasons and simplicity of creating plots
    matrix = [[choices([0, 2], weights = [1-p, p]) for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[i][j][0]

    return matrix

if __name__ == '__main__':
    # This tests whether simple matrix has only 0 and 2 in it
    test_matrix = creat_matrix(5, 0.5)
    for i in range(len(test_matrix)):
        for j in range(len(test_matrix[i])):
            assert test_matrix[i][j] == 0 or test_matrix[i][j] == 2