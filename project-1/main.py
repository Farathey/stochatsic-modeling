import matplotlib.pyplot as plt
from matrix import creat_matrix
from percolation import percolation
from os import mkdir, path
# mkdir and path functions from os module allow us to automaticly create directories

def predicted(p, n):
    '''
    Auxilary function to create plot of predicted values by the formula specified in the content of the task

    Atributes:
    ---------

    p : float
        probability

    n : int
        dimension of matrix 
    '''
    return (1-p**n)**n

list_prob = []
# We will run 10 independent trials and then calulate average for each probability
for i in range(10):

    # Here we declare auxilary lists for calulating averages for each probability in each sampling
    prob = [] # for y values
    p_test2 = [] # for x values

    # We will sample for each probability from 0.0 to 1.0 with step = 0.01
    p = 0.0
    while p < 1.0:

        # Here we declare auxilary variables for calulations and file naming
        dim = 50 # the dimension of matrix -> it will be dim x dim
        p_name = int(p*1000)
        summ = 0
        times = 100 #it's the number of samples we'll generate for each probability value

        # Here we check if whether given directory exists - if it doesn't we create it with name according to scheme:
        # p(probability*100)(dimension of matrix)(number of trial)
        if path.isdir(f'.\\plots\\p{p_name}{dim}{i}') == False:
            mkdir(f'.\\plots\\p{p_name}{dim}{i}')

        # Here we begin our sampling
        for j in range(times):
            # We create our matrix
            open_matrix = creat_matrix(dim, p)

            # Then we create its plot
            plt.matshow(open_matrix, cmap = 'plasma')
            plt.title(f'p = {p}, dim = {dim}x{dim}')
            
            # Instead of showing it will save it to the created eariler direcotries with names according to scheme:
            # p(probability*100)(dimension of matrix)(number of trial)(number of sample)open.png
            plt.savefig(f'.\\plots\\p{p_name}{dim}{i}\\p{p_name}{dim}{i}{j}open.png')
            plt.close() # and we have to close it due to limitations of matplotlib to opening max 20 plots at once
            # plt.show()

            # We run our percolation finction to check whether our system percolates
            value, full_matrix = percolation(open_matrix)

            # Here we create plot for filled matrix
            plt.matshow(full_matrix, cmap = 'plasma')
            plt.title(f'p = {p}, dim = {dim}x{dim}')
            # And also instead of showing it we save it with name according to scheme
            # p(probability*100)(dimension of matrix)(number of trial)(number of sample)full.png
            plt.savefig(f'.\\plots\\p{p_name}{dim}{i}\\p{p_name}{dim}{i}{j}full.png')
            plt.close()
            # plt.show()

            # Here we increment value for calulating the average of times in which our system percolates
            if value == True:
                summ += 1

        # And Here we calculate the average, append it to auxilary list and increment our probability
        # print(summ/times)
        prob.append(summ/times)
        p_test2.append(p)
        # and here we increment probability
        p += 0.01

    # Here we print list of averages from all samples for each probability
    print(prob)
    
    # Here we append list of probabilities for each p to list, to calculate the average for all 10 runs
    list_prob.append(prob)

# Here we calculate the average by taking the value for each probability from each run, summing them and dividing by number of runs
average = [] # y values
x = [] # x values
iterator = 0.0
for j in range(len(list_prob[0])):
    suma = 0
    for i in range(len(list_prob)):
        suma += list_prob[i][j]
    average.append(suma/len(list_prob))
    x.append(iterator)
    iterator += 0.01

# Here we create values for plot of predicted values
p = 0.0
n = 50
test = []
p_test = []

while p < 1.0:
    test.append(predicted(p, n))
    p_test.append(p)
    p += 0.001

# First we create bar plot for averaged values from all the runs 
plt.bar(x, average, width=0.01, align='edge', color = '#4F9CED', edgecolor = '#95C3F4', linewidth = 2, zorder = 3)
# As second we create plot for predicted values
plt.plot(p_test, test, c = 'red', linewidth = 2, zorder = 3)
# Cosmetics
plt.grid(axis='y')
plt.title('Corelation between 1 occuring in the system and its percolation')
plt.xlabel('Probability of 1 occuring in system')
plt.ylabel('Probability of system percolating')
plt.legend(['predicted distribution = (1-p^n)^n'], loc = 'lower left')
plt.show()