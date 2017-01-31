from flask import Flask, render_template, request, Response
from tinydb import TinyDB, Query, where

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#    return 'Hello World!'


@app.route('/')
def serve_html():
    db = TinyDB('db.json')
    colours = db.all()[0]

    return render_template('index.html', red=colours['red'], green=colours['green'], blue=colours['blue'])


@app.route('/postData', methods=['POST'])
def post_data():
    blue = request.form.get('blue')
    green = request.form.get('green')
    red = request.form.get('red')

    db = TinyDB('db.json')
    db.purge() # TODO: dont purge
    db.insert({'red': red, 'green': green, 'blue': blue})

    

    return Response(response="ok", status="200")

@app.before_first_request
def before_req():
    db = TinyDB('db.json')

    if len(db.all()) == 0:
        db.insert({'red': 128, 'green': 128, 'blue': 128})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80")

