from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('logo.html')

@app.route('/login',methods=['GET'])
def login():
    account = request.args["acc"]
    password = request.args["pword"]
    namelist = {'user1':'password1'}
    if(account in namelist and password == namelist[account]):
        return '登入成功'
    else: return '登入失敗'

if __name__ == '__main__':
    app.debug = True
    app.run()