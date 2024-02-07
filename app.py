from flask import Flask,render_template,redirect
import random

app = Flask(__name__, static_folder="./static/")

# 自己紹介Webページを作成しましょう

@app.route('/')
def index():
    # ランダムなカラーコードを作成
    color = "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    # 生成されるのは#7890ABのようなコード
    return render_template('index.html', color=color)

@app.route('/link1')
def link1():
    return render_template('link.html')

@app.route('/link2')
def link2():
    return redirect('/')

if __name__=='__main__':
    app.run(host="0.0.0.0",port=80,debug=False)