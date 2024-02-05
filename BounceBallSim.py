# This is a simulation of a ball bouncing 
# Takes into consideration gravity and loss of energy to surroundings after each bounce

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Constants
dt = 0.1
t = 0
g = 9.8
u = 0
height = 25
ballRadius = 0.564
bounceFactor = 0.7
stopBounce = 2 * math.sqrt((2*height)/g) * (1/(1-bounceFactor) + 0.5)

# Lists for Storing Data
heightVals = []
timeVals = []

# Function to update the plot for each frame
def update(frame):
    global t, height, u, ballRadius

    heightVals.append(height)
    timeVals.append(t)

    t += dt
    height -= ((u*dt) + 0.5*g*dt**2)
    u = u + g*dt

    if t >= stopBounce:
        height = ballRadius
        ani.event_source.stop()

    if height < ballRadius:
        height = ballRadius
        u = - (u * bounceFactor)
      
    scat.set_offsets([[t, height]])

    # To keep ball in centre of graph
    ax.set_xlim(max(0, t - 1.5), max(3, t + 1.5))
    return scat,

# Sets up the plot
fig, ax = plt.subplots()
scat = ax.scatter([], [], c='b', s=100, label="Moving Ball")
ax.set_xlim(0, 2)
ax.set_ylim(0, height+5)
ax.set_xlabel("Time")
ax.set_ylabel("Height")
ax.set_title("Bouncing Ball Animation")
ax.legend()

# Creates the animation
ani = FuncAnimation(fig, update, frames=range(5000), interval=1, repeat=False)

plt.show()

