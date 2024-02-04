# This is the second part of my Monte Carlo estimate for pi 
# Here, I use the matplotlib library to visualise the process

import random
import matplotlib.pyplot as plt

n = 130

inCirc = 0
inCircX = []
inCircY = []

outCirc = 0
outCircX = []
outCircY = []

for _ in range(n ** 2):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    distFromOrigin = (x ** 2 + y ** 2)

    if distFromOrigin <= 1:
        inCirc += 1
        inCircX.append(x)
        inCircY.append(y)

    else:
        outCirc += 1
        outCircX.append(x)
        outCircY.append(y)

ratio = inCirc / (outCirc + inCirc)
piEstimate = ratio * 4

plt.scatter(inCircX, inCircY, c='blue', marker='+', alpha=0.7)
plt.scatter(outCircX, outCircY, c='red', marker='+', alpha=0.7)
plt.title("Monte Carlo Estimate for Pi")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

print(f"Estimate for pi is: {piEstimate}")
plt.show()
