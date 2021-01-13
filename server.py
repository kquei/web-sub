from flask import Flask
from setting import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_DATABASE_URI
db = SQLAlchemy(app)


class Ss(db.Model):
    # 定义表名
    __tablename__ = 'sub_hash'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sub_hash = db.Column(db.String(255))


@app.route('/sub')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
