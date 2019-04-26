import flask
import pickle
import pandas as pd
app = flask.Flask(__name__)

#-------- MODEL GOES HERE -----------#

# pipe = pickle.load(open("pipe.pkl","rb"))

#-------- ROUTES GO HERE -----------#

dummy = pd.read_csv('../data/dummy.csv')

# This method takes input via an HTML page
@app.route('/page')
def page():
    return flask.render_template('page.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

        player_move = flask.request.form['player_move']
        computer_move = 3


#        data = pd.DataFrame([{
#            'grape': grape}])

        # pred = pipe.predict(data)[0]
        # results = {'quality': round(pred, 1)}
        return flask.render_template('in_play.html', tables=[dummy.to_html(classes='data')], titles=dummy.columns.values, player_move=player_move, computer_move=computer_move)
        #f'player move is {player_move}, the bot chose {computer_move}'
        #return flask.jsonify(results)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 4000

    app.run(HOST, PORT)
