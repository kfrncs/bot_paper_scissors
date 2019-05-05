# ignore future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# joblib to save the model
import joblib

# ML imports
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
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

# train test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.33, random_state=42)

# RANDOM FORESTS
rf = RandomForestClassifier()
print("training RandomForestClassifier")
rf.fit(X_train, y_train)
print('random forest train score: ', rf.score(X_train, y_train))
print('random forest test score: ', rf.score(X_test, y_test))

# CATBOOST
cb = CatBoostClassifier()
print("training CatBoostClassifier")
cb.fit(X_train, y_train, plot=False, logging_level='Silent')
print('catboost score on train: ', cb.score(X_train, y_train))
print('catboost score on test: ', cb.score(X_test, y_test))

# KNeighbors
kn = KNeighborsClassifier()
print("training KNeighborsClassifier")
kn.fit(X_train, y_train)
print('K neighbours score on train: ', kn.score(X_train, y_train))
print('K neighbours on test: ', kn.score(X_test, y_test))

# defining variables for CrossValidation
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
bootstrap = [True, False]
random_grid = {'n_estimators': n_estimators,
               'max_depth': max_depth,
               'bootstrap': bootstrap}

rf_random = RandomizedSearchCV(estimator = rf,
                               param_distributions = random_grid,
                               n_iter = 50,
                               cv = 3,
                               verbose=2,
                               random_state=42)

# commented out to save time on next run
# rf_random.fit(X_train, y_train)

# but these were the results:
# {'n_estimators': 800, 'max_depth': 10, 'bootstrap': False}
# rf_random.best_params_

# RANDOM FORESTS REDUX
# increases score to 39.5% from ~37%
rf = RandomForestClassifier(n_estimators=800,
                            max_depth=10,
                            bootstrap=False)
print("retraining RandomForestClassifier")
rf.fit(X_train, y_train)
print('random forest train score: ', rf.score(X_train, y_train))
print('random forest test score: ', rf.score(X_test, y_test))

print("saving model to rock_paper_forests.joblib")
joblib.dump(rf, 'rock_paper_forests.joblib')

print("saving clean dataframe")
df.to_csv('data/rock_paper_clean.csv', index=False)
