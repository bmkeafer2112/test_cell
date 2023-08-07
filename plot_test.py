# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 13:30:24 2023

@author: AMTAdmin
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
 
fig = plt.figure(figsize=(6, 3))
x = [0]
y = [0]
 
ln, = plt.plot(x, y, '-')
 
def update(frame):
    x.append(x[-1] + 1)
    y.append(randrange(0, 10))
 
    ln.set_data(x, y) 
    fig.gca().relim()
    fig.gca().autoscale_view() 
    return ln,
 
animation = FuncAnimation(fig, update, interval=500)
plt.show()