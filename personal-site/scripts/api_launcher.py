# coding:utf-8
from flask import Flask;
from flask import make_response;
from flask import request;
import MySQLdb;
import MySQLdb.cursors;
import json;
import edit_home;

app = Flask(__name__);

@app.route("/api/beanyon/articles")
def get_articles():
    db = MySQLdb.connect(host="localhost",user="root",passwd="y1054639005",db="beanyon",use_unicode=True,charset="utf8",cursorclass=MySQLdb.cursors.DictCursor);
    cursor = db.cursor();
    cursor.execute("select title,description,create_time,create_addr from articles");
    #articles = [(dict(title=row[1],description=row[2],create_time=row[3],create_addr=row[4]) for row in cursor.fetchall())];
    articles = cursor.fetchall();
    db.close();
    json_articles = json.dumps(articles);
    rst = make_response(json_articles);
    rst.headers['Access-Control-Allow-Origin']='*';
    rst.headers['Access-Control-Allow-Method']='GET';
    rst.headers['Access-Control-Allow-Headers']='x-requested-width,content-type';
    return rst;

@app.route("/api/beanyon/info")
def get_info():
    db = MySQLdb.connect(host="localhost",user="root",passwd="y1054639005",db="beanyon",use_unicode=True,charset="utf8",cursorclass=MySQLdb.cursors.DictCursor);
    cursor = db.cursor();
    cursor.execute("select * from beanyon_info");
    info = cursor.fetchone();
    db.close();
    json_info = json.dumps(info);
    rst = make_response(json_info);
    rst.headers['Access-Control-Allow-Origin']='*';
    rst.headers['Access-Control-Allow-Method']='GET';
    rst.headers['Access-Control-Allow-Headers']='x-requested-width,content-type';
    return rst;

@app.route("/api/beanyon/manager/receivepic", methods=['POST'])
def receive_showpic():
    print request;
    if request.method == 'POST':
        pic = request.files['file'];
        print request;
        print pic;
    info = {"result": "true"};
    json_info = json.dumps(info);
    rst = make_response(json_info);
    rst.headers['Access-Control-Allow-Origin']='*';
    rst.headers['Access-Control-Allow-Headers']='x-requested-width,content-type';
    return rst;

@app.route("/api/beanyon/manager/home", methods=['POST'])
def edit_home_info():
    info = {"result": "false", "title": "编辑失败", "message": "您的编辑失败，请检查数据后再次尝试"};
    if request.method == 'POST':
        title = request.form['title'];
        content = request.form['content'];
        tail = request.form['tail'];
        owner = request.form['owner'];
        label = request.form['label'];
        edit_home.edit(title,content,tail,owner,label);
        info = {"result": "true", "title": "编辑成功", "message": "数据已经成功保存"};
    json_info = json.dumps(info);
    rst = make_response(json_info);
    rst.headers['Access-Control-Allow-Origin']='*';
    rst.headers['Access-Control-Allow-Headers']='x-requested-width,content-type';
    return rst;

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True);
