import numpy as math
import imageio
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# work in standard units of meters, seconds, and radians

l = 1
m = 1
g = 9.81


# initialize length and mass of pendulum
# Lagrangian is given as T-V = 1/2m(l^2)(omega)^2 - mglcos(theta)
# Solving Euler-Lagrange, we get ml^2alpha = mglsin(theta), or alpha = gsin(theta)/l

def derivative(y, t, l, m):
    theta, omega = y
    # insert derivative as defined by Euler-Lagrange
    dydt = [omega, - 0.5 * omega - (g / l) * math.sin(theta)]
    return dydt


# give initial conditions for pendulum, theta given in degrees
theta_naught, omega_naught = 179, 10

# create an array of times for the process, followed by initial conditions
intervals = 100
seconds = 10
t = math.linspace(0, seconds, intervals)
y_naught = math.array([theta_naught * math.pi / 180, omega_naught])

# create vector array y with theta and omega for at any time
solution = odeint(derivative, y_naught, t, args=(l, m))
x = []
y = []

# change to cartesian coordinates
for i in range(intervals):
    x.append(l * math.sin(solution[i][0]))
    y.append(-l * math.cos(solution[i][0]))


# function creates frames at each portion of time
def create_frame(r):
    # plot the pendulum and the bar connecting to the origin
    plt.plot(x[r], y[r], marker="o", markersize=7, markeredgecolor="red", markerfacecolor="black")
    plt.plot([x[r], 0], [y[r], 0], 'k-')
    # add axis preferences and titles to graph
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.xticks([])
    plt.yticks([])
    seconddisplay = (r / intervals) * seconds
    seconddisplay= round(seconddisplay, 2)
    plt.title(f'Pendulum position at {seconddisplay} seconds')
    plt.savefig(f'img_{r}.png')
    plt.close()


# calls function for frames, creating at different times throughout motion
for r in range(intervals):
    create_frame(r)
frames = []
# appends all frames into an array and uses imageio to make it into a gif
for r in range(intervals):
    image = imageio.v2.imread(f'img_{r}.png')
    frames.append(image)
# resultant gif is saved

imageio.mimsave('./example.gif', frames, fps=15)

