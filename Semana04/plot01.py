import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

plt.scatter(x,y)
plt.show()

x1 = np.arange(-1000,1000,1)
y = x1**2

plt.plot(x1,y)
plt.show()