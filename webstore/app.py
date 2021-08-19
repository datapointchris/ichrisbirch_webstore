from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/orders/', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return render_template('orders.html')
    
    if request.method == 'POST':
        order = request.get_json
        print(order)
        



if __name__ == '__main__':
    app.run()
