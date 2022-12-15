from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# # http://127.0.0.1:5000/address
@app.route('/images', methods=["GET"])
def address_get():

    return 


@app.route('/upload', methods=["POST"])
def address_post():
    file = request.files['file']
    file.save("./static/images/" + file.filename , "wb")
    return 

# http://127.0.0.1:5000/ 
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)