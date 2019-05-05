# third, random bot
import random
import joblib

class KenBot:
    def __init__(self, model_joblib):
        self.history = {'player': [], 'bot': []}
        self.model = joblib.load(model_joblib)
        self.game_count = 0

    def capture(self, y):
        self.history['player'].append(y)

    def predict(self):
        y = random.choice([1, 2, 3])
        self.history['bot'].append(y)
        return y

    def throw(self, y):
        x = self.model.predict(y)
        self.capture(y)
        return x
