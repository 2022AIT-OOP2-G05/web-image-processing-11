# web-image-processing-11

## 作ろうとしているプログラム
このプログラムは未完成である．
画像のアップロードを行うWebインターフェイスと、アップロードされた画像のファイル変更を検知して画像処理を行う画像処理プログラムを組み合わせたシステムの構築をしようとしている
<br>
## 使用した言語，ライブラリのバージョン
Python 3.10.6
cv2 version 4.6.0
Flask2.2.2
<br>
## ファイルの説明

main.py
それぞれ画像を返却するAPIを作成。json形式で画像の保存先のpathを返す

gs.py
画像のグレースケール処理

2chika.py
画像の2値化

frame.py
カスケード分類器を使用して、画像の中に顔があるのか判定してあったら、顔を枠で囲む

face_mosaic.py
顔検出器を用いて顔を検出し検出した顔にモザイクかける

canny-filter.py
入力画像を読み込み，読み込んだ画像をグレースケール化する
グレースケール化した画像をcannyフィルターによって輪郭を抽出する

main.js
画像を投稿する処理を記載とイベントリスナーの登録。

components/base-components
htmlのtemplateタグから要素の読み込みそれの描画を行うための処理を記述した抽象クラス。

components/header.js
処理後の画像を表示するHTMLのHeader部分の読み込みと表示。base-componentsを継承している。

Components/main-item.js
処理後の画像の一覧を表示するところの読み込みと表示を行う。base-componentsを継承し、読み込んだ画像を１つずつ表示している。画像を受け取る。
fetchもこのclassで呼び出している。

components/item.js
画像１つ分を表示する。base-componentsを継承しておりmain-item.jsで画像の数だけインスタンス化される。

main-load.js
上記のcomponentsフォルダで作成したクラスをインスタンス化するクラス。

Pages/*.js
それぞれの画像に対応するmain-load.jsをインスタンス化する。URLによって読み込む画像を指定している。

Utils/fetch.js
main.pyから画像を取得するためのfetchの処理が書かれているクラス。
<br>
## できていないこと
・画像処理ファイル(gs.py, 2chika.py, frame.py, face_mosaic.py, canny-filter)が複数の画像に対応していない
・投稿完了の表示、画像の名前の入力
