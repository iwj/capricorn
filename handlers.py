# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-03-05
# Author: juzi
# E-mail: jentlewoo@gmail.com


from views import *

#就是一些路径映射配置

HANDLERS = [(r"/", IndexHandler), 
        (r"/login", LoginHandler),
        (r"/edit", EditHandler), 
        (r"/read", ReadHandler), (r"/help", HelpHandler),
        (r"/logout", LogoutHandler),
        (r"/reg", RegisterHandler),
        (r"/account", AccountHandler),
        (r"/search", SearchHandler),
        ]
