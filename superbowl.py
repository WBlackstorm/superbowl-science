import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('superbowl.csv')
df.info()
df.head()
df.describe()
df.drop(['SB', 'Winner', 'Loser', 'MVP', 'Stadium', 'City', 'State'], axis='columns', inplace=True)
df.head()

df['Total Points'] = df['Winner Pts'] + df['Loser Pts']
df.head()

df['year'] = pd.to_numeric(df['Date'].str.slice(start=-4))
df.drop('Date', axis=1, inplace=True)
df.head()

plt.boxplot(df['Total Points'])
plt.title("Total Points per Match", loc="center", fontsize=14)
plt.show()

plt.boxplot([df["Winner Pts"], df["Loser Pts"]])
plt.title("Winner Points / Loser Points", loc="center", fontsize=14)
plt.show()

plt.scatter(df.loc[df['year'] < 1980]['Winner Pts'], df.loc[df['year'] < 1980]['Loser Pts'])
plt.title("Winner Points / Loser Points 60's - 70's", loc="center", fontsize=14)
plt.show()

plt.scatter(df.loc[(df['year'] >= 1980) & (df['year'] < 2000)]['Winner Pts'], df.loc[(df['year'] >= 1980) & (df['year'] < 2000)]['Loser Pts'])
plt.title("Winner Points / Loser Points 80's - 90's", loc="center", fontsize=14)
plt.show()


plt.scatter(df.loc[(df['year'] >= 2000)]['Winner Pts'], df.loc[(df['year'] >= 2000)]['Loser Pts'])
plt.title("Winner Points / Loser Points 00's", loc="center", fontsize=14)
plt.show()

fig, ax = plt.subplots()
decades = ['60s', '70s', '80s', '90s', '00s', '10s']
points = [0, 0, 0, 0, 0, 0]
index = 0
for year in df['year']:
    if year < 1970:
        points[0] += df.loc[index]["Total Points"]
    if year >= 1970 and year < 1980:
        points[1] += df.loc[index]["Total Points"]
    elif year >= 1980 and year < 1990:
        points[2] += df.loc[index]["Total Points"]
    elif year >= 1990 and year < 2000:
        points[3] += df.loc[index]["Total Points"]
    elif year >= 2000 and year < 2010:
        points[4] += df.loc[index]["Total Points"]
    else:
        points[5] += df.loc[index]["Total Points"]
    index += 1

ax.bar(decades, points)
plt.title("Points at Superbowl by decades", loc="center", fontsize=14)
plt.show()