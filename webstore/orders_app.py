from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask is working, make your post'


if __name__ == '__main__':
    app.run()
