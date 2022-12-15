from flask import Flask, make_response, render_template, request, url_for, redirect,jsonify
import os
import re


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# # http://127.0.0.1:5000/address
@app.route('/images', methods=["GET"])
def address_get(): 
    # 画像ファイルのパスをjsonで返す
    patternStr = '.+\.(jpg|png|jpeg|heic)'
    pattern = re.compile(patternStr)
    
    # with open('./web-interface/url.json') as f:
    #         json_data = json.load(f)
    # jsonの作成
    json_data = []
    for file in os.listdir('./web-interface/static/changed-images'):
        if pattern.match(file):
            json_data.append({
                "url": "../static/changed-images/" + file,
            })

    print(json_data)
    return jsonify(json_data)

    









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