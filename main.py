from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/say')
def user_message():
    word = request.args.get("word")
    if not word:
        return "Please give some url parameter. Ex: ?word='This is I'"
    return word


if __name__ == '__main__':
    app.run()
