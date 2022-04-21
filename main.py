"""This is simple flask app. Can be used like template"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Serve homepage"""
    return 'Welcome!'


if __name__ == '__main__':
    app.run()
