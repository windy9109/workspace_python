from flask import Flask
from flask.globals import request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/", methods=['POST'])


# def hello_world():
#     # get 방식
#     a = request.args.get('a')
#     #a = request.args.post('a')
#     return 'Hello, Python'+a


def post():
    a = request.form.get('a')
    msg = "Hello, World!" +a
    return msg


if __name__ == '__main__':
    app.run()
    #debug=True