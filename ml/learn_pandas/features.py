import pandas as pd

df = pd.DataFrame({
    'T1': [10, 15, 8],
    'T2': [25, 27, 25],
    'T3': [17, 22, 19],
})

print('{}\n'.format(df))

print('{}\n'.format(df.sum()))

print('{}\n'.format(df.sum(axis=1)))

print('{}\n'.format(df.mean()))

print('{}\n'.format(df.mean(axis=1)))
