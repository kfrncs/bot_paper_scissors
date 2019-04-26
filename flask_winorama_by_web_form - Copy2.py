
import flask

app = flask.Flask(__name__)

import pandas as pd
import pickle


# def train():
#     target = "p2"
#     df = df[~df[target].isnull()]
#     y = df[target]
#     X = df.drop(target, axis=1)
#     X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42)
#     X_train.head()
#     mapper = DataFrameMapper(
#         [
#             (["id"], [SimpleImputer(strategy="mean"), StandardScaler()]),
#             (["p1"], [SimpleImputer(strategy="mean"), StandardScaler()]),
#             ("p2", [SimpleImputer(strategy="mean"), StandardScaler()]),
#         ],
#         df_out=True,
#     )

#     X_train_m = mapper.fit_transform(X_train)
#     X_test_m = mapper.transform(X_test)
#     model = LinearRegression()
#     model.fit(X_train_m, y_train)
#     model.score(X_train_m, y_train)
#     model.score(X_test_m, y_test)



#-------- MODEL GOES HERE -----------#
pipe = pickle.load(open("pipe.pkl", "rb"))

# sugar = 4
# sulphates = 2
# alcohol = 13
# grape = 'red'


# new_data = pd.DataFrame(
#     [{"sugar": sugar, 
#     "sulphates": sulphates, 
#     "alcohol": alcohol, 
#     "grape": grape}]
# )

# pipe.predict(new)



#-------- MODEL GOES HERE -----------#

import flask
app = flask.Flask(__name__)

@app.route('/page')
def page():
   with open("page.html", 'r') as page:
       return page.read()

# def empty():
#     df = pd.DataFrame({
#     "id": [], 
#     "p1": [],
#     "p2": [],
#     })
#     df.to_csv('data/rock2.csv', index= False)




@app.route('/result', methods=['POST', 'GET'])
def result():
    
    if flask.request.method == 'POST':
        df = pd.DataFrame({
        "id": [], 
        "p1": [], 
        "p2": [], 
        })

        inputs = flask.request.form
        p1 = inputs['p1']
        # print(inputs)
        df['p1'] = p1
        # df['p1'].append(inputs['p1'])

        df.to_csv('data/rock2.csv', index= False)

        # return "Hello World!"
        return flask.jsonify(results)


#-------- ROUTES GO HERE -----------#
if __name__ == '__main__':
    # '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = 4000

    app.run(HOST, PORT)

