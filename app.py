from flask import Flask, jsonify
from lib.finance import Yahoo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/finance/<string:code>')
def get_finance_data(code):
    return jsonify(Yahoo.get_finance_data(code))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
