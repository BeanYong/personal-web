#!/usr/bin/python
#-*- coding:utf-8 -*-
import MySQLdb;
import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

class Saver: 
    def save(self, title, description, create_time):    
        db = MySQLdb.connect(host="localhost",user="root",passwd="y1054639005",db="beanyon",use_unicode=True,charset="utf8");
        cursor = db.cursor();
        insert_article = "insert into articles(title,description,create_time,create_addr) values('%s','%s','%s','%s')" % (title,description.strip(),create_time,"南昌大学前湖校区");
        try:
            cursor.execute(insert_article);
            db.commit();
            print "insert success";
        except Exception,e:
            print repr(e);
            print "insert failed";
            db.rollback();
        db.close();
