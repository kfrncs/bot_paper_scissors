import pandas as pd
import numpy as np

# ML imports
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
import marky as mk

df = pd.read_csv('data/rock_paper.csv')

# last 5 turns by player one are stored in a column each
for i in range(1,6):
    df[f'p1_-{i}'] = df.groupby('game_id')['player_one_throw'].shift(i)

# check what player two threw last, which gets a column
df['p2_last'] = df.groupby('game_id')['player_two_throw'].shift(i)

# make df['y'] the *next* throw - for test
df['y'] = df.groupby('game_id')['player_one_throw'].shift(-1)


# a move thrown at same time as Player 1 does not have any effect
# on what Player 1 played that turn
df.drop('player_two_throw', axis=1, inplace=True)

# drop game_id and game_round_id
# because we used them as much as we needed to
df.drop('game_id', inplace=True, axis=1)
df.drop('game_round_id', inplace=True, axis=1)

# drop any rows with missing values
df.dropna(inplace=True)

# take the test away
y = df['y']
df.drop('y', inplace=True, axis=1)
