from flask import Flask,render_template,redirect


app = Flask(__name__, static_folder="./static/")

# 自己紹介Webページを作成しましょう

@app.route('/')
def loginform():
    return render_template('index.html')

@app.route('/link1')
def link1():
    return render_template('link.html')

@app.route('/link2')
def link2():
    return redirect('/')

if __name__=='__main__':
    app.run(host="0.0.0.0",port=80,debug=False)