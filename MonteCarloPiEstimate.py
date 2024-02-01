# In this program, I estimate pi using the monte carlo estimation 
# This works by taking a unit circle (radius 1) inside a square and finding the ratio of the (circle area/square area * 4) to give pi
# My next step will be to show this graphicallly on matplotlib

import random

n = 10000 

inCirc = 0 
outCirc = 0 

for _ in range(n**2): 
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1) 

  distFromOrigin = (x**2 + y**2)**0.5

  if distFromOrigin <= 1: 
    inCirc += 1

  else: 
    outCirc += 1 

ratio = inCirc / (outCirc + inCirc) 
piEstimate = ratio * 4 

print("Estimate for pi is: ", piEstimate)
  




  
