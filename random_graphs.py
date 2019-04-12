from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def d2plot():
    fig = plt.figure()
    fig.suptitle("No axes on this figure") 
    fig, ax_lst = plt.subplots(1,1)
    x = np.linspace(0, 2, 100)

    plt.plot(x, x, label="linear")
    plt.plot(x, x**2, label="quadratic")
    plt.plot(x, x**3, label="cubic")
    plt.plot(x, np.sin(x), label="sin" )
    plt.plot(x, np.cos(x), label ="cos")
    

    plt.xlabel("x label")
    plt.ylabel("y label")

    plt.title("Simple Plot")

    plt.legend()

    plt.show()
    
    fig = plt.figure()
    fig.suptitle("No axes on this figure") 
    fig, ax_lst = plt.subplots(1,1)
    x = np.linspace(0, 2, 100)

    plt.plot(x, np.tan(x), label="tan")
    plt.plot()

    plt.xlabel("x label")
    plt.ylabel("y label")

    plt.title("Simple Plot")

    plt.legend()

    plt.show()
    
    fig = plt.figure()
    fig.suptitle("No axes on this figure") 
    fig, ax_lst = plt.subplots(1,1)
    x = np.linspace(0, 2, 100)

    plt.plot(x, np.tan(np.sin(x**3 * x**3 * x**3)), label="pattern")
    
    plt.xlabel("x label")
    plt.ylabel("y label")

    plt.title("Simple Plot")

    plt.legend()

    plt.show()
def d3plot():
    plt.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    plt.show()
    
d2plot()
d3plot()
