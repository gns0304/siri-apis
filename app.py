from flask import Flask, request, jsonify
from lib.finance import Investing

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/finance')
def get_finance_data():
    type = request.args.get("type")
    code = request.args.get("code")
    return jsonify(Investing.get_finance_data(type, code))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
