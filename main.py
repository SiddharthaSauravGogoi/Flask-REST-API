from flask import Flask
import pandas

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get_data")
def get_data():
    df = pandas.read_csv('data.csv')
    return df.to_json(orient="columns")

if __name__=="__main__":
	app.debug = True
	app.run(host='127.0.0.1', port=5000)