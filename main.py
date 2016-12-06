# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-01-08
# Author: juzi
# E-mail: jentlewoo@gmail.com


import os.path
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import torndb
from handlers import HANDLERS

define("mysql_host", default="127.0.0.1:3306")
define("mysql_database", default="post")
define("mysql_user", default="root")
define("mysql_password", default="")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            debug = True,
            handlers = HANDLERS,
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            cookie_secret="WgS2xI3hT2WluCLhz+Sk9Stq6pXnt0xGsJomGGITDHk=",
            xsrf_cookies = True,
            login_url = "/login",
            )
    app.db = torndb.Connection(
            host = options.mysql_host, database = options.mysql_database,
            user = options.mysql_user, password = options.mysql_password
            )
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
