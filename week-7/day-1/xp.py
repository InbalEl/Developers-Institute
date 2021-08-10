import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print('-----------EX 1--------------')
def create_np_array(start, length, step) -> np.array:
    return np.arange(start, (start + step*length), step)

a1 = create_np_array(6, 100, 4)
print(a1)

print('-----------EX 2--------------')
a2 = np.array([1,2,3,np.nan,5,6,7,np.nan])
print(a2)

a2 = a2[~np.isnan(a2)]
print(a2)

print('-----------EX 3--------------')
a3 = np.random.randint(1, 100, size=(5,6))
print(a3)

print('-----------EX 4--------------')
series1 = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
print('-------------')
print(series1)
print('-------VALUE COUNT------')
print(series1.value_counts())

print('-----------EX 5--------------')
series2 = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
print('-------------')
print(series2)
series2 = pd.to_datetime(series2)
print(series2.dt.day)
print(series2.dt.week)
print(series2.dt.dayofyear)
print(series2.dt.dayofweek)

print('-----------EX 6--------------')
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print('------READ CSV-------')
print(df)
print(df.count())

df = df.rename(columns={'Type':'TypeOfCar'})
print(df.head())
print(df.isnull().sum())
print(max(df.isnull().sum()))

print('-----------EX 7--------------')
del df['EngineSize']
df.drop('Length', 1, inplace=True)
print(f'Is EngineSize in df columns? {"EngineSize" in df.columns}')
print(f'Is Length in df columns? {"Length" in df.columns}')
print(df.head())

print('-----------EX 8--------------')

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

print(df1)
print('-----------')
print(df2)

#df3 = pd.DataFrame.merge(df1, df2, left_index=True, right_index=True)
#print(df3)

df1.merge(df2, left_on='fruit', right_on='pazham').drop_duplicates()
print('-----------')
print(df1)

print('-----------EX 9--------------')

df4 = pd.DataFrame(["STD,City\tState",
"33,Kolkata\tWest Bengal",
"44,Chennai\tTamil Nadu",
"40,Hyderabad\tTelengana",
"80,Bangalore\tKarnataka"], columns=['row'])

print(df4)
string_series = df4.iloc[:,0]
print(string_series)

df4[['STD', 'City\tState']] = string_series.str.split(",", n=1,expand=True)
df4[['City', 'State']] = string_series.str.split("\t", n=1,expand=True)
del df4['row'], df4['City\tState']
print(df4)

print('-----------EX 10--------------')

names = ["mpg", "cylinders", "displacement", "horsepower",
         "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data",
                     header=None, names=names, delim_whitespace=True)

#- displacement over x-axis
#- acceleration over y-axis


def scatter_plot(df: pd.DataFrame, x_col_name: str, y_col_name: str) -> None:

    plt.style.use('seaborn')
    plt.title(f'{x_col_name}-{y_col_name} Corelation')

    plt.xlabel(x_col_name)
    plt.ylabel(y_col_name)
    plt.scatter(df[x_col_name], df[y_col_name])
    plt.tight_layout()
    plt.show()

#scatter_plot(df_mpg, 'displacement', 'acceleration')

print('-----------EX 11--------------')

def bar_plot(df: pd.DataFrame, col_name: str) -> None:

    filtered_df = df_mpg[(df_mpg['model_year'] == 78) & (df_mpg['car_name'].str.contains('Toyota', case=False))]

    plt.style.use('fivethirtyeight')
    plt.bar(filtered_df['car_name'], filtered_df[col_name])

    plt.title(f'{col_name} Comparison')
    plt.show()

#bar_plot(df_mpg, 'cylinders')

print('-----------EX 12--------------')

def line_plot(df: pd.DataFrame) -> None:

    filtered_df = df_mpg[df_mpg['car_name'].str.contains('Toyota', case=False)]

    print(filtered_df)

    plt.style.use('fivethirtyeight')

    plt.plot(filtered_df['model_year'], filtered_df['weight'])

    plt.title('Toyota car weight over time')
    plt.show()

# line_plot(df_mpg)

print('-----------EX 13--------------')

filtered_df = df_mpg[df_mpg['car_name'].str.contains('audi', case=False)]

print(filtered_df)

plt.style.use('seaborn')

plt.plot(filtered_df['model_year'], filtered_df['acceleration'])

plt.title('Audi ecceleration over time')
plt.show()