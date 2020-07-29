import numpy as np
import matplotlib.pyplot as plt
x = 10
x1 = pow(x,2)
x2 = pow(x,3)
theta = 45
y1 = np.sin(theta)
y2 = np.cos(theta)
meshPoints = np.linspace(-1, 1, 500)
meshPoints1 = meshPoints[53]
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()
