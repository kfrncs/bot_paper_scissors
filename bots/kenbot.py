# third, random bot
import random
import joblib
import pandas as pd

class KenBot:
    def __init__(self, model_joblib):
        self.history = {'player': [], 'bot': []}
        self.model = joblib.load(model_joblib)
        self.game_count = 0

    def capture(self, y):
        self.history['player'].append(y)
        pass

    def predict(self):
        y = random.choice([1, 2, 3])
        self.history['bot'].append(y)
        return y

    def throw(self):
        # x = self.model.predict(self.df)

        if self.game_count < 10:
            x = random.choice([1, 2, 3])
            self.history['bot'].append(x)
            pass
        elif self.game_count == 10:
            # TODO: this is where we will create the past five turns df

            x = random.choice([1, 2, 3])
            self.history['bot'].append(x)
            self.create_df()
            print('dataframe created')
            # x = bot.throw(results)
            pass
        else:
            #TODO:
            # append this turn to the DF created
            # print(bot.df)
            # x = bot.predict(bot.df) #
            pass
        self.game_count += 1
        return x

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

        self.df = self.df[['player_one_throw',
                           'p1_-1',
                           'p1_-2',
                           'p1_-3',
                           'p1_-4',
                           'p1_-5',
                           'p2_last']]

        # and drop the first row (it doesn't have a p2_last)
        self.df = self.df.drop(range(0,4))


        return self
