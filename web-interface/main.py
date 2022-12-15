from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# # http://127.0.0.1:5000/address
# @app.route('/', methods=["GET"])
# def address_get():
#     return 


# @app.route('/address', methods=["POST"])
# def address_post():


#         return 

# http://127.0.0.1:5000/ 
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)