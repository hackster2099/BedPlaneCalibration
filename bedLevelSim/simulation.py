import matplotlib.pyplot as plt
import os
import sys
import threading as thread
import numpy as np
from mpl_toolkits import mplot3d
from pathlib import Path
from numpy.linalg import inv

def calculation(dataFile):
    
    # picking the 3D axes system for the project
    axis = plt.axes(projection="3d") # making a 3d axes 

    # collecting the data from the available txt file in the CSV format
    dataPoints = np.loadtxt(dataFile, delimiter=",")
    

    # Seperation of the data by the columns
    xDataMeas = dataPoints[:,0]
    yDataMeas = dataPoints[:,1]
    zDataMeas = dataPoints[:,2]

    # printing the sample data
    print(zDataMeas)


    # creating a constant value for c as 1, since we dont know the current value of it and trying to calculate it
    c_ConstantValue = np.ones_like(xDataMeas)

    # making a matrix of the collected data
    A = np.column_stack((xDataMeas,yDataMeas, c_ConstantValue ))
    
    # obtaining the transpose of matrix A in order to use it for calcualtion
    A_transpose = np.transpose(A)

    # calculated a,b,c values, using them for the equation of the plane 
    xVector = np.matmul(inv(np.matmul(A_transpose, A)), np.matmul(A_transpose, zDataMeas))

    print(f"a --> {xVector[0]}, b --> {xVector[1]}, c --> {xVector[2]}")

    # creating a referenace array data, for domain and range of 0-10, and using that to create a surface plane
    xDataRef = np.arange(0,10,1)
    yDataRef = np.arange(0,10,1)


    # Making a 3D array based on the axes increment domain and range given
    X_ref, Y_ref= np.meshgrid(xDataRef ,yDataRef)

    # Making a 3D array in the same size as X, but all elements being zero
    Z_ref = np.zeros_like(X_ref)

    # plotting a 3D surface based on the arrays given
    axis.plot_surface(X_ref,Y_ref,Z_ref, )

    # using the same xy plane data to complete the question of the plane now that the a,b,c values are obtained
    Z = xVector[0]*X_ref + xVector[1]*Y_ref + 0 # --> you can add xVector[2] for the full plane position drawing

    # plotting the plane for the reference 
    axis.plot_surface(X_ref,Y_ref,Z,)


    normalVector_graphed = np.array([-1*xVector[0], -1*xVector[1], 1])


    axis.quiver(0,0,0, normalVector_graphed[0], normalVector_graphed[1], normalVector_graphed[2], color="orange",
    arrow_length_ratio=0.50, length=3.5)

    axis.quiver(0,0,0, 0,0,1, color="blue", arrow_length_ratio=0.50, length=3.5)

    plt.show()


def main():

    if(len(sys.argv) != 2):

        print("ERROR --> wrong command type")
        print("\nCommand --> python3 pythonfile.py dataFile.txt")
        sys.exit(0)

    fileDirectory = Path.cwd() / sys.argv[1] 
    calculation(fileDirectory)

    #points = np.loadtxt()



if __name__ == "__main__":
    main()


