import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100,100)
print(x)
y = x ** 2
plt.grid()

plt.plot(x,y,'b--')
plt.show()