# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-01-18
# Author: juzi
# E-mail: jentlewoo@gmail.com


import tornado.web
import requests
import json

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        return self.get_secure_cookie("user")

class LoginHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.render("login.html", info="")
        else:
            self.render("login.html", info="已经登录"+self.current_user)

    def post(self):
        get_username = self.get_argument("username")
        get_password = self.get_argument("password")
        sql = "select username from user where username=%s and password=%s"
        ret = self.db.query(sql, get_username, get_password)
        if not ret:
            self.render("login.html", info="用户名或密码错误")
        else:
            self.set_secure_cookie("user", ret[0]["username"])
            self.redirect(self.get_argument('next', '/'))

class LogoutHandler(BaseHandler):
    def get(self):
        if(self.get_argument("action", None)):
            self.set_secure_cookie("user", "");
            self.redirect("/")
        else:
            self.redirect("/")

class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

class IndexHandler(BaseHandler):
    def get(self):
        sql = "select * from article order by id desc limit 5;"
        ret = self.db.query(sql)
        self.render("index.html", article=ret)

class EditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render(
                "edit.html",
                info="",
                draft_title="",
                draft_text="",
                )

class UploadHandler(BaseHandler):
    def post(self):
        try:
            get_title = self.get_argument("edit_title")
            get_text = self.get_argument("edit_text")
            get_code = self.get_argument("invite_code")
            if(get_code == "CA45TZ"):
                if(get_title == "" or get_text == ""):
                    self.render("edit.html",
                        info="邀请码正确，标题和内容都为必填项",
                        draft_title = get_title,
                        draft_text = get_text)
                else:
                    #self.db.execute()
                    sql = 'insert into article(title, text, author, tag_main, \
                    tag_sub, post_date, post_time) values(%s, %s, %s, "微信", "normal", CURRENT_DATE, CURRENT_TIME);'
                    self.db.execute(sql, get_title, get_text, "wujian")
                    self.render("edit.html",
                        info="邀请码正确，两种内容都已提交",
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
    def get(self,):
        id = self.get_argument("id", 1)
        sql = "select * from article where id="+str(id)
        ret = self.db.query(sql)
        if(ret):
            ret_title = ret[0]["title"]
            ret_text = ret[0]["text"]
            ret_time = ret[0]["post_date"]
        else:
            ret_title = "文章未找到"
            ret_text = "<p>请检查网址是否有误</p><a href='/'>去往首页</a>"
            ret_time = "如有问题请反馈给我们"
        self.render(
                "read.html",
                title = ret_title,
                time = ret_time,
                text = ret_text,
                )

class HelpHandler(BaseHandler):
    def get(self,):
        bing_json = ("http://cn.bing.com/HPImageArchive.aspx?"
                "format=js&idx=0&n=1&nc=1444634662901&pid=hp")
        print bing_json
        result = requests.get(bing_json).text
        result_dict = json.loads(result)
        image_url = result_dict.get("images")[0].get("url")
        image_copyright = result_dict.get("images")[0].get("copyright")
        page_words = "<img src='%s'>" % (image_url) + image_copyright
        self.render("help.html", arg = page_words)
