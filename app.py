from collections import Counter
import numpy as np
from flask import Flask, request, render_template
import pandas as pd
import random

import joblib
from utils import emoji_to_num, num_to_words, evaluate
from bots.kenbot import KenBot

app = Flask(__name__)

game_count = 0
game = {}

bot = KenBot('bots/rock_paper_forests.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        player_throw = emoji_to_num(request.form['player_throw'])
        bot.capture(player_throw)
        bot_throw = bot.throw()

        result = evaluate(player_throw, bot_throw)

        # increases win/loss/tie, or creates them if they don't exist
        if result == 'win' and ('wins' in game):
            game['wins'] += 1
        elif result == 'win' and (not 'wins' in game):
            game['wins'] = 1
        elif result == 'lose' and ('losses' in game):
            game['losses'] += 1
        elif result == 'lose' and (not 'losses' in game):
            game['losses'] = 1
        elif result == 'tie' and (not 'ties' in game):
            game['ties'] = 1
        else:
            game['ties'] += 1

        # Calculates win % if there is enough data
        if 'wins' in game and 'losses' in game and 'ties' in game:
            game['win_pct'] = game['wins'] / (game['wins'] + game['losses'] + game['ties'])
        elif 'wins' in game and 'losses' in game:
            game['win_pct'] = game['wins'] / (game['wins'] + game['losses'])
        elif 'wins' in game and 'ties' in game:
            game['win_pct'] = game['wins'] / (game['wins'] + game['ties'])
        else:
            game['win_pct'] = 0

        # round the win %
        game['win_pct'] = round((game['win_pct'] * 100), 2)

        # pass results to the game dict for flask
        game['results'] = result
        game['player'] = num_to_words(player_throw)
        game['bot'] = num_to_words(bot_throw)
    return render_template('index.html', game=game)

current_market = {}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
