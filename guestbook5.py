from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:SPYatb32373@node1247-rachpython.th.app.ruk-com.cloud:5432/testdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:YKHvca91771@node17329-panumas.app.ruk-com.cloud:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    links = ['https://www.youtube.com', 'https://www.bing.com',
             'https://www.python.org', 'https://www.enkato.com']
    return render_template('example.html', links=links)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)