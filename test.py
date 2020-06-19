from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/info/price', methods=['POST'])
def get_price():
    min_price = 123123123
    max_price = 345345346456

    return min_price, max_price

print(get_price())
print('*'*80)




if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)