# third, random bot
import random

class KenBot:
    def __init__(self):
        self.history = {'player': [], 'bot': []}

    def capture(self, y):
        self.history['player'].append(y)

    def predict(self):
        y = random.choice([1, 2, 3])
        self.history['bot'].append(y)
        return y

    def throw(self, y):
        x = self.predict()
        self.capture(y)
        return x