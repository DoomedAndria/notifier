from flask import Flask
from main import run

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>oka<h1/>"


if __name__ == '__main__':
    app.run()
    run()
