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

#from tornado.options import define, options
#define("port", default=8000, help="run port", type=int)
define("mysql_host", default="127.0.0.1:3306")
define("mysql_database", default="test")
define("mysql_user", default="root")
define("mysql_password", default="")

#################################################

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers = HANDLERS,
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static")
            )
    app.db = torndb.Connection(
            host = options.mysql_host, database = options.mysql_database,
            user = options.mysql_user, password = options.mysql_password
            )
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
