from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

global order_list
order_list = []


@app.route('/')
def home():
    return render_template('order.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    """
    1. 주문 받기 API 만들기
    - 주문자 성함, 수량, 주소, 전화번호를 받아서 딕셔너리로 만든 다음, 글로벌 변수에 리스트로 저장하기
    """

    if request.method == "POST":
        name = request.form['name']
        count = request.form['count']
        address = request.form['address']
        phone = request.form['phone']

        # 딕셔너리로 만들어서
        order_dict = {'name': name, 'count': count, 'address': address, 'phone': phone}

        # global 변수에 리스트로 저장
        order_list.append(order_dict)

    return render_template('order.html')

# 주문 보기
@app.route('/list', methods = ['GET'])
def list():
    return jsonify(order_list)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)