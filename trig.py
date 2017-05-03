#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt


def integrate(y, dx):
    return np.dot(y, dx)

# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y
x = np.arange(0, np.pi, 0.01)

y_sin = np.sin(x)
plt.figure(1)
plt.title('y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y_sin)


y_cos = np.cos(x)
plt.figure(2)
plt.title('y=cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y_cos)

dx = np.full(x.shape, 0.01)
print("result of integrate(y, dx):")
print("sin:", integrate(y_sin, dx))
print("cos:", integrate(y_cos, dx))

print("result of numpy.trapz:")
print("sin:", np.trapz(y_sin, dx=0.01))
print("cos:", np.trapz(y_cos, dx=0.01))

plt.show()
