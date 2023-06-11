import pandas as pd
import numpy as np

# A dataframe is created from a list of lists

df = pd.DataFrame()
# Newline added to separate DataFrames
print('{}\n'.format(df))

df = pd.DataFrame([5, 6])
print('{}\n'.format(df))

df = pd.DataFrame([[5, 6]])
print('{}\n'.format(df))

df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])
print('{}\n'.format(df))

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                  index=['r1', 'r2'])
print('{}\n'.format(df))
upcast = pd.DataFrame([[5, 6], [1.2, 3], [3, 7]])
print('{}\n'.format(upcast))
# Datatypes of each column
print(upcast.dtypes)
df = pd.DataFrame([[5, 6], [1.2, 3]])
ser = pd.DataFrame([[0, 0]])

df_app = pd.concat([df, ser])
print('pd.concat {}\n'.format(df_app))

df_app = pd.concat([df, ser], ignore_index=True)
print('pd.concat {}\n'.format(df_app))

df2 = pd.DataFrame([[0, 0], [9, 9]])
df_app = pd.concat([df, df2])
print('pd.concat {}\n'.format(df_app))
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
# Drop row r1
df_drop = df.drop(labels='r1')
print('{}\n'.format(df_drop))

# Drop columns c1, c3
df_drop = df.drop(labels=['c1', 'c3'], axis=1)
print('{}\n'.format(df_drop))

df_drop = df.drop(index='r2')
print('{}\n'.format(df_drop))

df_drop = df.drop(columns='c2')
print('{}\n'.format(df_drop))

df.drop(index='r2', columns='c2')
print('{}\n'.format(df_drop))
