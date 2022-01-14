import numpy as np
import matplotlib.pyplot as plt
import math

#lucky seed ;)
np.random.seed(888) #set seed to have a reproducible experiment at first

# We want to approach pi as the number of points in the circle divided by the number of points in the square will approach pi.

def genererXY(s):
    """ToDo: rand includes numbers from [0, 1) but in this we are asked for both sides to be included
        I didn't find how to include the right side of the equation..."""
    #generate a random number in the [-1,1] range for x and y
    x = 2 * np.random.rand(s) - 1
    y = 2 * np.random.rand(s) - 1

    #return x, y tuple of lists
    return x, y

#methodMonteCarlo
def monteCarlo(size_of_array):
    """ use the x^2+y^2<=r^2 to specify where a
        specific point lands i.e if it lands
        inside the circle or outside the circle
        (inside of the square)"""

    x, y = genererXY(size_of_array) #try with a small size

    #we've decided the number of points generated from the onset,
    #so we only need to find out how many points are in the circle
    #and divided by the total number of points


    circle_numpy_array = x**2 + y**2

    in_circle = 0
    for val in (circle_numpy_array):
        if val <= 1:
            in_circle+=1

    return in_circle

def printResults():
    num_pts_in_c_list = []
    errors_list = []
    for pt in range(100, 10001, 100):
        num_pts_in_c = monteCarlo(pt)
        ratio_pts_in_out_c = num_pts_in_c/pt
        print(f"For {pt} in total: {num_pts_in_c} were inside the circle\n" + 
                f" the ratio between the # of points inside of the circle to the number " +
                f" of points outside of the circle is {ratio_pts_in_out_c}")

        num_pts_in_c_list.append(num_pts_in_c)
        ratio_pts_in_out_c -= (math.pi / 4)
        errors_list.append(ratio_pts_in_out_c)

    return num_pts_in_c_list, errors_list

#calculate the error of our prediction
def plotGraphOfErrors(num_pts_in_c_list, errors_list):
    plt.title("Error made by the monte Carlo method")
    plt.xlabel("nombre de points")
    plt.ylabel("erreur")
    plt.plot(num_pts_in_c_list, errors_list, color='red')
    plt.savefig('errors.png')



