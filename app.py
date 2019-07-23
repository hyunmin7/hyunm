from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/order', methods=['GET'])
def order():
    name = request.form['name']

    return jsonify({'name': name})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
