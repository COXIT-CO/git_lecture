from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/say')
def hello_world():
    word = request.args.get("word")
    return word


if __name__ == '__main__':
    app.run()
