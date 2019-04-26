import flask
import pickle
import pandas as pd
app = flask.Flask(__name__)

#-------- MODEL GOES HERE -----------#

# pipe = pickle.load(open("pipe.pkl","rb"))

#-------- ROUTES GO HERE -----------#

# This method takes input via an HTML page
@app.route('/page')
def page():
   with open("page.html", 'r') as page:
       return page.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

        player_move = flask.request.form['player_move']

#        data = pd.DataFrame([{
#            'grape': grape}])

        # pred = pipe.predict(data)[0]
        # results = {'quality': round(pred, 1)}
        return f'player move is {player_move}'
        #return flask.jsonify(results)

@app.route('/predict', methods=["GET"])
def predict():
    grape = flask.request.args['grape']

    data = pd.DataFrame([{
        'grape': grape}])

    # pred = pipe.predict(data)[0]
    # results = {'quality': round(pred, 1)}
    return None

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 4000

    app.run(HOST, PORT)
