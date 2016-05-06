#!/usr/bin/python

import json
import sys
import matplotlib.pyplot as plt

with open ('games.json', 'r') as fp:
  games = json.load(fp)


sorted_games = games.items()

sorted_games.sort(key=lambda tup: tup[1])
topten = sorted_games[-10:]

x_val = [data[0] for data in topten]
y_val = [data[1] for data in topten]

plt.bar(range(len(x_val)), y_val, align='center')
plt.title("Top 10 Games on Dicetower Top 10 Lists")
plt.xlabel("Games")
plt.ylabel("Number of List Appearances")
plt.xticks(range(len(topten)), x_val, rotation=0, fontsize='6')

plt.show()
