from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient 
app = Flask(__name__)

client = MongoClient('mongodb+srv://lxTraining:learningx@cluster0.xi7oq7q.mongodb.net/?retryWrites=true&w=majority')
db = client.buyinglandmars

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    nama_receive = request.form['nama_give']
    alamat_receive = request.form['alamat_give']
    ukuran_receive = request.form['ukuran_give']

    doc = {
        'Nama' : nama_receive,
        'Alamat' : alamat_receive,
        'Ukuran' : ukuran_receive,
    }
    db.pembeli.insert_one(doc)
    return jsonify({'msg': 'Data Berhasil Tersimpan'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list = list(db.pembeli.find({}, {'_id' : False}))
    return jsonify({'pembeli': orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)