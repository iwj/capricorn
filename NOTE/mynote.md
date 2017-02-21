# My note by TimeLine

## MySQL:2016-2-16

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
而自己却报错：
Cant connect to local MySQL server through socket '/var/mysql/mysql.sock' (2)
很奇怪。
唯一不同的是，视频里在官网下载tar压缩包解压的，自己是用brew工具安装的，不知道是不是这个原因。

## 理解&总结

2016-2-16
安装好之后需要配置my.cnf
而在segmentfault看到一个回答用brew命令也可以启动mysql，很奇怪。
暂时先用brew命令启动，先调试网站吧

## MySQL:2016-2-16

尝试在项目中使用MySQL

使用homebrew顺利安装。但是在启动MySQL服务时遇到问题，
使用mysql －u命令尝试登录时一直提示找不到sock
而对mysql不了解的我，完全不知道这是怎么一回事。
在网上查了一番，seagmentfault上一个问答里，发现使用brew命令也可以启动mysql，也下载了XAMPP。

第二天，开电脑后发现，使用mysql －u 命令可以正常登录。真是奇怪。
不知道是重启了才使其服务运行起来，还是XAMPP带来的效果。

## MySQL:2016-2-18

MySQL建表时发现极度缺乏相关知识，只知道对应列应该用何种数据类型、长度等因素
是否该为NULL这个方面的了解则不够深，没有透彻地了解NULL其目的、如何应用


## MySQL:2016-3-1

mysql建表
tornado的登录功能（实现登录后登录注册按钮消失）

## MySQL:2016-3-5

用户表的设计
字段    类型        是否空      其他
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
id      int         NOT NULL    AUTO_INCREMENT
用户名  varchar(10) NOT NULL
密码    varchar(10) NOT NULL

实际操作：
mysql> create table user(
        -> id int not NULL auto_increment,
        -> username varchar(10) not NULL,
        -> password varchar(10) not NULL,
        -> PRIMARY KEY (id));
Query OK, 0 rows affected (0.33 sec)

    mysql> desc user;
    +----------+-------------+------+-----+---------+----------------+
    | Field    | Type        | Null | Key | Default | Extra          |
    +----------+-------------+------+-----+---------+----------------+
    | id       | int(11)     | NO   | PRI | NULL    | auto_increment |
    | username | varchar(10) | NO   |     | NULL    |                |
    | password | varchar(10) | NO   |     | NULL    |                |
    +----------+-------------+------+-----+---------+----------------+
    3 rows in set (0.01 sec)

## torndb:2016-3-6

sudo pip install torndb 之后
在ipython里测试 import torndb 报错，No module named MySQLdb
Google之后在stackoverflow查到：
sudo pip install mysql-python
之后再去ipython测试，正常。

## MySQL: 2016-4-2

建第2张表，存储文章

设计
字段    类型        是否空      其他
－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
id      int         NOT NULL    AUTO_INCREMENT
title   varchar(20) NOT NULL    -
text    TEXT        NOT NULL    -
date    date        NOT NULL
time    time        NOT NULL
author  varchar(10) NOT NULL    -
tag     varchar(30) NOT NULL

实际操作：
mysql> create table article( id INT not NULL auto_increment, title varchar(20)
NOT NULL, text TEXT NOT NULL, date DATE NOT NULL, time TIME NOT NULL,
author varchar(10) NOT NULL, tag varchar(30) NOT NULL,PRIMARY KEY (id));
Query OK, 0 rows affected (0.19 sec)

描述：
mysql> desc article;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| title  | varchar(20) | NO   |     | NULL    |                |
| text   | text        | NO   |     | NULL    |                |
| date   | date        | NO   |     | NULL    |                |
| time   | time        | NO   |     | NULL    |                |
| author | varchar(10) | NO   |     | NULL    |                |
| tag    | varchar(30) | NO   |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

## Front-End:2016-4-13

textarea的内容存入数据库再取出来，回车就消失了。
解决方案：
wangEditor＋直接存HTML代码段

## MySQL:2016-8-10

在新电脑上配置依赖的环境，

安装MySQL时，使用homebrew安装，安装完成后mysql －uroot无法启动

在segmentfault上看到这样的信息：

brew info mysql

在终端输入以上的命令之后，返回的几行信息里有一句熟悉的命令：

brew services start mysql

之后再mysql -uroot 就能进入了。

地址：https://segmentfault.com/q/1010000000094608

目前，仍无法熟悉MySQL安装相关遇到的问题啊，都是遇到问题解决了但无法知其根本原因

## 2016-09-15 update the table: article

mysql> create table article(
    -> id int not null auto_increment,
    -> title varchar(20) not null,
    -> text text not null,
    -> post_date DATE NOT NULL,
    -> post_time TIME NOT NULL,
    -> author varchar(10) NOT NULL,
    -> tag_main varchar(10) NOT NULL,
    -> tag_sub varchar(10) NOT NULL,
    -> PRIMARY KEY (id));
Query OK, 0 rows affected (0.02 sec)

mysql> desc article;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| title     | varchar(20) | NO   |     | NULL    |                |
| text      | text        | NO   |     | NULL    |                |
| post_date | date        | NO   |     | NULL    |                |
| post_time | time        | NO   |     | NULL    |                |
| author    | varchar(10) | NO   |     | NULL    |                |
| tag_main  | varchar(10) | NO   |     | NULL    |                |
| tag_sub   | varchar(10) | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
8 rows in set (0.01 sec)

因表设计时，没有添加自动插入时间，所以在sql 语句里添加日期时间：

mysql> insert into article(title, text, author, tag_main, tag_sub, post_date, post_time) values("It is a title", "lalala", "WuJian", "微信", "normal", CURRENT_DATE, CURRENT_TIME);
Query OK, 1 row affected (0.00 sec)

mysql> select * from article;
+----+---------------+--------+------------+-----------+--------+----------+---------+
| id | title         | text   | post_date  | post_time | author | tag_main | tag_sub |
+----+---------------+--------+------------+-----------+--------+----------+---------+
|  1 | It is a title | lalala | 2016-09-15 | 16:06:21  | WuJian | 微信     | normal  |
+----+---------------+--------+------------+-----------+--------+----------+---------+
1 row in set (0.00 sec)


## 2017-02-20 run on Ubuntu 16.04

1. install tornado and torndb
2. install mysql
http://www.dengzhr.com/node-js/866
3. install python-mysqldb
thanks! https://stackoverflow.com/questions/454854/no-module-named-mysqldb

run it.
