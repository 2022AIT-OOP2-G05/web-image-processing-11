import io
from flask import Flask, make_response, render_template, request, url_for, redirect
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# # http://127.0.0.1:5000/address
@app.route('/images', methods=["GET"])
def address_get(): 
    from PIL import Image
    filename = 'example.jpg'
    img = Image.open(filename)
    img_bin = io.BytesIO(request.data).getvalue() # 受信
    response = make_response(img_bin) # レスポンスに画像を設定
    response.headers.set('Content-Type', request.content_type) # ヘッダ設定
    return 


@app.route('/upload', methods=["POST"])
def address_post():
        file = request.files['file']
        file.save(os.path.join('./web-interface/static/images', file.filename))
        return redirect(url_for('index'))

# http://127.0.0.1:5000/ 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show')
def show():
    return render_template("show.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)