# third, random bot
import random
import joblib
import pandas as pd

class KenBot:
    def __init__(self, model_joblib):
        self.history = {'player': [], 'bot': []}
        self.model = joblib.load(model_joblib)
        self.game_count = 0
        self.win_dict = {
            1: 2,
            2: 3,
            3: 1
        }

    def capture(self, y):
        self.history['player'].append(y)
        pass

    def predict(self):
        # Get a prediction of what the player will throw
        # using RandomForestsClassifier
        y = self.model.predict(self.df)
        # fetch last value from list of predictions
        y = y[-1]
        print(f"y is {y}")
        return self.win_dict.get(y)

    def throw(self):
        # first 10 games are random, not from the model
        # this is an issue that could be fixed with a different implementation
        if self.game_count < 10:
            x = random.choice([1, 2, 3])
            self.history['bot'].append(x)
            pass
        elif self.game_count == 10:
            x = random.choice([1, 2, 3])
            self.history['bot'].append(x)
            self.create_df()
            print('dataframe created')
            pass
        else:
            print('Game count: ', self.game_count)
            x = self.predict()
            self.history['bot'].append(x)
            self.append_turn()
            # print(bot.df)
            # x = bot.predict(bot.df) #
            pass
        self.game_count += 1

        return x

    def append_turn(self):
        append_df = pd.DataFrame({
            'player_one_throw': self.history['player'][-1],
            'p1_-1': self.history['player'][-2],
            'p1_-2': self.history['player'][-3],
            'p1_-3': self.history['player'][-4],
            'p1_-4': self.history['player'][-5],
            'p1_-5': self.history['player'][-5],
            'p2_last': self.history['bot'][-2]
        }, index=[self.game_count])

        self.df = self.df.append(append_df, ignore_index=True)
        return self

    def create_df(self):
        print(f"length bot: ", len(self.history['bot']))
        print(f"length player: ", len(self.history['bot']))

        self.df = pd.DataFrame({
            'player_one_throw': self.history['player'],
            'p2_last': self.history['bot'] # bot's last turn.. almost
        })

        # make p2_last last turn instead of current
        self.df['p2_last'] = self.df['p2_last'].shift(1)

        # add the p1 history columns
        for i in range(1,6):
            self.df[f'p1_-{i}'] = self.df['player_one_throw'].shift(i)

        # reorder columns
        self.df = self.df[['player_one_throw',
                           'p1_-1',
                           'p1_-2',
                           'p1_-3',
                           'p1_-4',
                           'p1_-5',
                           'p2_last']]

        # and drop the first row (it doesn't have a p2_last)
        self.df = self.df.drop(range(0,5))


        return self
