from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient


Client = MongoClient('localhost', 27017)
db = Client.dbsparta

app = Flask(__name__)


@app.route('/mypage')
def mypage():
    return render_template('index.html')


@app.route('/link')
def link():
    return render_template('link.html')


@app.route('/get-card')
def get():
    cardList = db.articles.find({}, {'_id': 0})
    print(cardList)
    return jsonify({"result": "success", "articles": list(cardList)}) #list는 배열형으로 만들어줌
    # 저장된 데이터를 리스트로 가공해서 보여줌. DB에서 꺼내온 데이터는 가공을 거쳐서 보여줘야함.

@app.route('/post-card', methods=["POST"])
def post():

    print(request.form)
    url = request.form['url']
    comment = request.form['comment']

    dic = {"url": url, "comment": comment}

    db.articles.insert_one(dic)

    print(dic)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)