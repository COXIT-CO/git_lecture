"""This is simple flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """This is main route"""
    return 'Hello World'


if __name__ == '__main__':
    app.run()
