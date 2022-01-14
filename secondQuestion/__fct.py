import numpy as np
import matplotlib.pyplot as plt

def collatz(n,count):
    """the collatz function screams for recursion to be used
        we can add to a count variable because functions 
        act as a stack."""
    if n == 1: 
        return count
    if not n % 2:
        count += 1
        return collatz(n/2, count)
    if n % 2:
        count += 1
        return collatz(3*n+1, count)

def generatePlots():
    count = 0
    x = np.arange(1, 5000) #start with a small number
    y = np.array([collatz(xi, count) for xi in x])
    plt.figure()
    plt.title("collatz conjecture")
    plt.xlabel("starting_point")
    plt.ylabel("number_of_iterations_till_convergence")
    plt.scatter(x, y)
    plt.savefig("collatz_scatter.png")
    
    #generate histogram, we need to call plt.figure
    #to seperate the two different plots from being 
    #in the same buffer
    plt.figure()
    plt.title('frequency_of_iterations')
    plt.ylabel('count_of_number_of_iterations')
    plt.xlabel('number_of_iterations')
    bins=np.arange(0,300,5)
    plt.hist(y, bins=bins, alpha=0.5, histtype='bar', ec='black')
    plt.savefig("collatz_histogram.png")






