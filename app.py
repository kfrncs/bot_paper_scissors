from collections import Counter
import numpy as np
from flask import Flask, request, render_template

import joblib
from utils import emoji_to_num, evaluate

app = Flask(__name__)
model = joblib.load('') 
results = []

# choose random row to play from for the first five turns
rand_row = np.random.randint(1,50000)
df.iloc[rand_row:rand_row+5]

@app.route('/', methods=['GET', 'POST'])
def index():
    game = {}
    if request.method == 'POST':
        player_throw = emoji_to_num(request.form['player_throw'])
        bot_throw = bot.throw(player_throw) # replace me
        result = evaluate(player_throw, bot_throw)
        results.append(result)
        game['result'] = result
        game['player'] = player_throw
        game['bot'] = bot_throw
    return render_template('index.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
