# %%
1 = rock
2 = paper
3 = scissors
# imports
0 = no input
# %%
import pandas as pd
import numpy as np
import pymc3 as pm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier

# ignore future warning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# read data
df = pd.read_csv('data/rock_paper.csv')

# make dummy df for predictions
dummy = df.head(1).copy()
# %%
# make columns with the last turn, two turns ago
df['p1_t-1'] = df.groupby('game_id')['player_one_throw'].shift(1)
df['p1_t-2'] = df.groupby('game_id')['player_one_throw'].shift(2)
df['p1_t-3'] = df.groupby('game_id')['player_one_throw'].shift(3)
df['p1_t-4'] = df.groupby('game_id')['player_one_throw'].shift(4)
df['p1_t-5'] = df.groupby('game_id')['player_one_throw'].shift(5)
df['p2_t-1'] = df.groupby('game_id')['player_two_throw'].shift(1)
df['p2_t-2'] = df.groupby('game_id')['player_two_throw'].shift(2)
df['p2_t-3'] = df.groupby('game_id')['player_two_throw'].shift(3)
df['p2_t-4'] = df.groupby('game_id')['player_two_throw'].shift(4)
df['p2_t-5'] = df.groupby('game_id')['player_two_throw'].shift(5)

# make y the next throw
y = df.groupby('game_id')['player_one_throw'].shift(-1)

# fill NaN's with 0's
df = df.fillna(0)
y = y.fillna(0)
# %%
df.sample()
# %%
# train test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.33, random_state=42)
# %%
# RANDOM FORESTS
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
print('random forest train score: ', rf.score(X_train, y_train))
print('random forest test score: ', rf.score(X_test, y_test))
# %%
# CATBOOST
cb = CatBoostClassifier()
cb.fit(X_train, y_train, plot=True, logging_level='Silent')
print('catboost score on train: ', cb.score(X_train, y_train))
print('catboost score on test: ', cb.score(X_test, y_test))
# %%
dummy = pd.read_csv('data/dummy.csv')
# %%

# %%

# %%

# %%
