from collections import Counter
import numpy as np
from flask import Flask, request, render_template
import pandas as pd
import random

import joblib
from utils import emoji_to_num, evaluate
from bots.kenbot import KenBot

app = Flask(__name__)

game_count = 0

bot = KenBot('bots/rock_paper_forests.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    game = {}
    if request.method == 'POST':

        player_throw = emoji_to_num(request.form['player_throw'])
        bot.history['player'].append(player_throw)

        bot_throw = bot.throw()

        result = evaluate(player_throw, bot_throw)

        # TODO: append results to dataframe
        # results.append(result)

        game['results'] = result
        game['player'] = player_throw
        game['bot'] = bot_throw
    return render_template('index.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
