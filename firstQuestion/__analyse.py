from __fct import plotGraphOfErrors
from __fct import printResults

def main():
    num_pts_in_c_list,errors_list = printResults()
    plotGraphOfErrors(num_pts_in_c_list, errors_list)

if __name__ == "__main__":
    main()

