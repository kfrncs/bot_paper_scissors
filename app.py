from collections import Counter
import numpy as np
from flask import Flask, request, render_template
import pandas as pd
import random

import joblib
from utils import emoji_to_num, evaluate
from bots.kenbot import KenBot 

app = Flask(__name__)
bot = KenBot('bots/rock_paper_forests.joblib')
# read blank.csv as template for game data
results = pd.read_csv('data/blank.csv')
game_count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    game = {}
    if request.method == 'POST':
        # choose random row to play from for the first five turns
        # rand_row = np.random.randint(1,50000)
        # df.iloc[rand_row:rand_row+5]
        player_throw = emoji_to_num(request.form['player_throw'])

        # under game 5 we throw randomly, otherwise we call bot.throw()
        if bot.game_count < 5:
            bot_throw = random.choice([1, 2, 3]) 
        elif bot.game_count == 5:
            # TODO: this is where we will create the past five turns df
            print('error out on game 5')
            bot_throw = bot.throw(results)
            pass
        else:
            bot_throw = bot.throw(results) # 
        
        bot.game_count += 1
        
        result = evaluate(player_throw, bot_throw)

        # TODO: append results to dataframe
        # results.append(result)

        game['results'] = result
        game['player'] = player_throw
        game['bot'] = bot_throw
    return render_template('index.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
