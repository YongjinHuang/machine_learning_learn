import pandas as pd

df = pd.read_csv('raw_data.txt')

groups = df.groupby('yearID')

for name, group in groups:
    print('Year: {}'.format(name))
    print('Group: {}'.format(group))
print('{}\n'.format(groups.get_group(2016)))
print('{}\n'.format(groups.sum()))
no2015 = groups.filter(lambda x: x.name > 2015)
print(no2015)

# player_df is predefined
groups = df.groupby(['yearID', 'teamID'])

for name, group in groups:
    print('Year, Team: {}'.format(name))
    print('{}\n'.format(group))

print(groups.sum())
