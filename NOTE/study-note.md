## MySQL

###启动MySQL

（一）https://segmentfault.com/q/1010000000475470
brew install mysql (安装)
添加修改mysql配置
mysqld --help --verbose | more (查看帮助, 按空格下翻)
你会看到开始的这一行(表示配置文件默认读取顺序)
Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /usr/local/etc/my.cnf ~/.my.cnf
通常这些位置是没有配置文件的, 所以要自己建一个
ls $(brew --prefix mysql)/support-files/my-* (用这个可以找到样例.cnf)
cp /usr/local/opt/mysql/support-files/my-default.cnf /etc/my.cnf (拷贝到第一个默认读取目录)
按需修改my.cnf
brew services start mysql (启动)
brew services stop mysql (停止)

(二)极客学院http://www.jikexueyuan.com/course/716_2.html?ss=1
==>
进入MySQL bin目录 cd usr/local/mysql/bin
mysql -u root (root 默认没有密码)
==>
以上是视频里的路径，本机的路径为usr/local/mysql／opt/bin
视频里直接在bin路径下就可以启动 mysql
而自己却报错：Cant connect to local MySQL server through socket '/var/mysql/mysql.sock' (2)
很奇怪。唯一不同的是，视频里在官网下载tar压缩包解压的，自己是用brew工具安装的，不知道是不是这个原因。

###理解&总结
2016-2-16
安装好之后需要配置my.cnf
而在segmentfault看到一个回答用brew命令也可以启动mysql，很奇怪。
暂时先用brew命令启动，先调试网站吧
