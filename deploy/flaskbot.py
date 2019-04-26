import flask
import pickle
import pandas as pd
import numpy as np
app = flask.Flask(__name__)

#-------- MODEL GOES HERE -----------#

# pipe = pickle.load(open("pipe.pkl","rb"))


# --- our functions ----------------#

computer_move = 0
amount_games = 0
draws = 0
player_wins = 0
computer_wins = 0
last_win = None
df = pd.DataFrame()
ID = []
p1 = []
p2 = []
df['ID'] = ID
df['p1'] = p1
df['p2'] = p2

def game(player_move):
    computer_move = np.random.randint(1,4)
    ID.append(len(p1))
    p1.append(player_move)
    p2.append(computer_move)
    for i in range(0,len(df)+1):
        df.loc[i] = [ID[i],p1[i],p2[i]]
    win_check(player_move, computer_move)
    return computer_move

def win_check(player_move, computer_move):
    if player_move == computer_move:
        draws += 1
        last_win = 'Nobody'
    elif (player_move == 1) and (computer_move == 2):
        # computer win
        computer_wins += 1
        last_win = 'Bot'
    elif (player_move == 1) and (computer_move == 3):
        player_wins += 1
        last_win = 'Player'
    elif (player_move == 2) and (computer_move == 1):
        player_wins += 1
        last_win = 'Player'
    elif (player_move == 2) and (computer_move == 3):
        computer_wins += 1
        last_win = 'Bot'
    elif (player_move == 3) and (computer_move == 1):
        computer_wins += 1
        last_win = 'Bot'
    elif (player_move == 3) and (computer_move == 2):
        player_wins += 1
        last_win = 'Player'
    else:
        print("Do you really want to play?")


#-------- ROUTES GO HERE -----------#

# This method takes input via an HTML page
@app.route('/page')
def page():
    return flask.render_template('page.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

        player_move = flask.request.form['player_move']
        computer_move = game(player_move)

#        data = pd.DataFrame([{
#            'grape': grape}])

        # pred = pipe.predict(data)[0]
        # results = {'quality': round(pred, 1)}
        return flask.render_template('in_play.html', tables=[df.to_html(classes='data')], titles=df.columns.values, player_move=player_move, computer_move=computer_move)
        #f'player move is {player_move}, the bot chose {computer_move}'
        #return flask.jsonify(results)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 4000

    app.run(HOST, PORT)
