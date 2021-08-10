import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analyse_array(arr: np.ndarray) -> tuple:
    return (np.amin(arr), np.std(arr) , np.prod(arr), np.dot(arr, arr), arr-4)

a1 = np.array([[0,1,2],[3,4,5],[6,7,8]])
#print(a1)

a1_analysis = analyse_array(a1)
#print(a1_analysis)

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
#print(df.head())
#print(df.info())
#print(df.describe())
print(df.iloc[50])

indices_list = [i for i in range(50,61,2)]

df2 = pd.DataFrame(df, columns=['species', 'petal_length','petal_width'], index=indices_list)
print(df2)

# TODO: how to?
#df3 = df['species', 'petal_length','petal_width'].iloc[50:61:2]

# TODO: how to?
#df4 = df.groupby('species').apply(np.sum)
#df5 = df.groupby('species').apply(np.mean)


# x = [1, 2, 3, 4]
# y = [2, 20, 35, 6]
# plt.plot(x, y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('first graph')
#plt.show()

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#print(dir(data))
plt.plot(data.columns, data["sepal_length"], "r--") 
plt.show()