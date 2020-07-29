import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 500)
#x1 = pow(np.exp,(-x/10))
#x2 = pow(exp, (-x/3))
f1 = np.exp(-x/10) * np.sin(np.pi * x)
f2 = x * np.exp(-x/3)
plt.plot(f1, x)
plt.plot(f2, x)
plt.show()




r0 = np.linspace(0, 1.2, 1000)
theta = np.linspace(-3.14, 3.14, 1000)
r = 1.2 + np.cos(theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure()
plt.plot(x,y)
plt.show()
