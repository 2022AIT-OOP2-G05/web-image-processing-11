from flask import Flask, make_response, render_template, request, url_for, redirect,jsonify
import os
import re
import uuid



app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

@app.route('/binarization', methods=["GET"])
def binarization_get(): 
    # 画像ファイルのパスをjsonで返す
    patternStr = '.+\.(jpg|png|jpeg)'
    pattern = re.compile(patternStr)
    
    print("a")
    json_data = []
    for file in os.listdir('./web-interface/static/images/binarization'):
        if pattern.match(file):
            src = "{}".format( url_for('static', filename='images/binarization/' + file) )
            id = str(uuid.uuid4())
            json_data.append({
                "src": src
                ,"id": id,
                "name": file
            })
    return jsonify(json_data)

@app.route('/face_mosaic', methods=["GET"])
def face_mosaic_get(): 
    # 画像ファイルのパスをjsonで返す
    patternStr = '.+\.(jpg|png|jpeg)'
    pattern = re.compile(patternStr)
    
    json_data = []
    for file in os.listdir('./web-interface/static/images/face_mosaic'):
        if pattern.match(file):
            src = "{}".format( url_for('static', filename='images/face_mosaic/' + file) )
            id = str(uuid.uuid4())
            json_data.append({
                "src": src
                ,"id": id,
                "name": file
            })
    return jsonify(json_data)

@app.route('/faceframe', methods=["GET"])
def faceframe_get(): 
    # 画像ファイルのパスをjsonで返す
    patternStr = '.+\.(jpg|png|jpeg)'
    pattern = re.compile(patternStr)
    
    json_data = []
    for file in os.listdir('./web-interface/static/images/faceframe'):
        if pattern.match(file):
            src = "{}".format( url_for('static', filename='images/faceframe/' + file) )
            id = str(uuid.uuid4())
            json_data.append({
                "src": src
                ,"id": id,
                "name": file
            })
    return jsonify(json_data)

@app.route('/gs', methods=["GET"])
def gs_get(): 
    # 画像ファイルのパスをjsonで返す
    patternStr = '.+\.(jpg|png|jpeg)'
    pattern = re.compile(patternStr)
    
    json_data = []
    for file in os.listdir('./web-interface/static/images/gs'):
        if pattern.match(file):
            src = "{}".format( url_for('static', filename='images/gs/' + file) )
            id = str(uuid.uuid4())
            json_data.append({
                "src": src
                ,"id": id,
                "name": file
            })
    return jsonify(json_data)


@app.route('/images', methods=["GET"])
def address_get(): 
    # 画像ファイルのパスをjsonで返す
    patternStr = '.+\.(jpg|png|jpeg)'
    pattern = re.compile(patternStr)
    
    json_data = []
    for file in os.listdir('./web-interface/static/images/input'):
        if pattern.match(file):
            src = "{}".format( url_for('static', filename='images/input/' + file) )
            id = str(uuid.uuid4())
            json_data.append({
                "src": src
                ,"id": id,
                "name": file
            })
    return jsonify(json_data)

@app.route('/upload', methods=["POST"])
def address_post():
    file = request.files['file']
    file.save(os.path.join('./web-interface/static/images/input', file.filename))
    return redirect(url_for('index'))

# http://127.0.0.1:5000/ 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show')
def show():
    return render_template("show.html")

@app.route('/binarization_temp')
def binarization():
    return render_template("binarization.html")

@app.route('/face_mosaic-temp')
def face_mosaic():
    return render_template("face_mosaic.html")

@app.route('/faceframe-temp')
def faceframe():
    return render_template("faceframe.html")

@app.route('/gs-temp')
def gs():
    return render_template("gs.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)