# ignore future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# ML imports
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from catboost import CatBoostClassifier

# load rock paper scissors game history data
df = pd.read_csv('data/rock_paper.csv')

# store last 5 turns by player 1 in separate columns
for i in range(1,6):
    df[f'p1_-{i}'] = df.groupby('game_id')['player_one_throw'].shift(i)

# check what player two threw last, which gets a column
df['p2_last'] = df.groupby('game_id')['player_two_throw'].shift(i)

# make df['y'] the *next* throw - for test
df['y'] = df.groupby('game_id')['player_one_throw'].shift(-1)

# drop player_two_throw:
#   a move thrown at same time as Player 1 does not have any effect
#   on what Player 1 played that turn
df.drop('player_two_throw', axis=1, inplace=True)

# drop game_id and game_round_id
# because we used them as much as we needed to
df.drop('game_id', inplace=True, axis=1)
df.drop('game_round_id', inplace=True, axis=1)

# drop any rows with missing values
df.dropna(inplace=True)

# store target values separately
y = df['y']
df.drop('y', inplace=True, axis=1)

# renumber index rows to prevent our model from learning from those
df.index = (range(0, len(df)))

df.sample(3)

# train test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.33, random_state=42)

# RANDOM FORESTS
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
print('random forest train score: ', rf.score(X_train, y_train))
print('random forest test score: ', rf.score(X_test, y_test))

# CATBOOST
cb = CatBoostClassifier()
cb.fit(X_train, y_train, plot=False, logging_level='Silent')
print('catboost score on train: ', cb.score(X_train, y_train))
print('catboost score on test: ', cb.score(X_test, y_test))

# KNeighbors
kn = KNeighborsClassifier()
kn.fit(X_train, y_train)
print('K neighbours score on train: ', kn.score(X_train, y_train))
print('K neighbours on test: ', kn.score(X_test, y_test))
