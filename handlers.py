# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-03-05
# Author: juzi
# E-mail: jentlewoo@gmail.com


from views import *

#就是一些路径映射配置

HANDLERS = [(r"/", IndexHandler), (r"/info", InfoHandler)]

HANDLERS += [(r"/login", LoginHandler)]

HANDLERS += [(r"/list", ListHandler)]

HANDLERS += [(r"/edit", EditHandler)]

HANDLERS += [(r"/upload", UploadHandler)]

HANDLERS += [(r"/read", ReadHandler)]
