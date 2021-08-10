import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0,11)
y = x**3
x2 = np.arange(0,11)
y2 = x**3/2

print(x,y,x2,y2,sep='\n')

plt.plot(x,y,color='r',label='first data', linewidth=5)
plt.plot(x2,y2,color='y',linewidth=5,label='second data')
plt.title('Multiline Chart')

plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.show()