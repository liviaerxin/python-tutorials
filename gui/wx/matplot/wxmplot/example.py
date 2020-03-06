#!/usr/bin/python
import numpy as np
x = np.linspace(0.0, 15.0, 151)
y = 5*np.sin(4*x)/(x*x+6)
z = 4.8*np.sin(4.3*x)/(x*x+8) + np.random.normal(size=len(x), scale=0.05)

import matplotlib.pyplot as plt
plt.plot(x, y, '-+', label='reference')
plt.plot(x, z, '-', label='signal')
plt.title('matplotlib example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()