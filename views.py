# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-01-18
# Author: juzi
# E-mail: jentlewoo@gmail.com


import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", title="登录")

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html", title="Tornado Application")

class InfoHandler(BaseHandler):
    def post(self):
        user = self.get_argument("arg1")
        password = self.get_argument("arg2")
        self.db.execute("insert into user(username,password) values(%s,%s)", user, password)
        self.render("info.html", arg1=user, arg2=password, title="info - mysql")

class ListHandler(BaseHandler):
    def get(self):
        ret = self.db.query("select * from user")
        self.render("list.html",arg = ret, title="all user")

class EditHandler(BaseHandler):
    def get(self):
        self.render(
                "edit.html", 
                info="文字尽可能通俗易懂 ;)", 
                draft_title="",
                draft_text=""
                )

class UploadHandler(BaseHandler):
    def post(self):
        try:
            get_title = self.get_argument("edit_title")
            get_text = self.get_argument("edit_text")
            # 临时用邀请码进行限制
            get_code = self.get_argument("invite_code")
            if(get_code == "CA45TZ"):
                if(get_title == "" or get_text == ""):
                    self.render("edit.html", 
                        info="邀请码正确，标题和内容都为必填项",
                        draft_title = get_title,
                        draft_text = get_text
                        )
                else:
                    #self.db.execute()
                    sql = "insert into article(title, text, author, tag) values(%s, %s, %s, %s)"
                    self.db.execute(sql, get_title, get_text, "admin", "['test', '测试']")
                    self.render("edit.html", 
                        info="邀请码正确,两种内容都已提交",
                        draft_title = get_title,
                        draft_text = get_text
                        )
            else:
                self.render(
                        "edit.html",
                        info="邀请码错误",
                        draft_title = get_title,
                        draft_text = get_text
                        )
        except ValueError:
            print ValueError

class ReadHandler(BaseHandler):
    def get(self):
        sql = "select * from article where id=%s"
        ret = self.db.query(sql,4)
        self.render(
                "read.html",
                title = "titile test",
                text = ret[0]["text"],
                time = ret[0]["posttime"]
                )
