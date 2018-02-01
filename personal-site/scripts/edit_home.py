#!/usr/bin/python
#-*- coding:utf-8 -*-
import MySQLdb;
import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

def edit(title, content, tail, owner, label):    
    db = MySQLdb.connect(host="localhost",user="root",passwd="y1054639005",db="beanyon",use_unicode=True,charset="utf8");
    cursor = db.cursor();
    insert_home = "insert into home_info(title,content,tail,owner,label) values('%s','%s','%s','%s','%s')" % (title,content,tail,owner,label);
    try:
        cursor.execute(insert_home);
        db.commit();
        print "insert success";
    except Exception,e:
        print repr(e);
        print "insert failed";
        db.rollback();
    db.close();
