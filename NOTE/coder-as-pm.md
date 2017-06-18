# TODO TimeLine

## 2016-3

- [x] Use tornado base.html
- [ ] format example :+1:

## 2016-4-2

- [x] HTML的缩进规范是怎样的 解决：选择2字符的方案
- [x] textarea 的固定 width
- [x] 站点顶部Logo Link的css样式
- [x] Add Navi area
- [x] Python的列表是否能直接存入MySQL（str 和 unicode 的问题） 解决：单个tag

## 2016-4-13

- [ ] Alpha版：具有阅读功能。文章暂时手动录入。现在要做的时先将程序部署到服务器，让测试用户
      开始测试，反馈UI、交互等的问题。
- [ ] 发布文章的功能下一版再实现。今天找到了开源的Web在线编辑器wangEditor，简单思考下，编辑
      器引入＋图片上传到图床等功能完善需要较多的时间。正好看到龙井老师发的一张图片，产品是一步
      步迭代每一次迭代都可用，而不是每次实现一个角落最后才可用。

## 2016-4-17

- [x] MySQL查询最近的记录

## 2017-01-03

- [ ] 安全问题：MySQL换掉root用户
- [ ] 注册页面的图形验证码
- [ ] 注册页面验证该邮箱是否已注册，若是，则提示是否忘记密码
- [ ] 自动保存草稿


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


# coding-as-pm

什么无人机、O2O、电动跑车等新事物脱颖而出，我们这一代人确实酷了，发现长辈们越来越难以理解这些，苦于不会使用。

本人的亲身经历，在跟父亲大人解说一个新事物时，他居然带有恐惧感。母亲大人看着身边的人都用微信，也想用，当我教她时，她总是推脱：“学东西要慢慢来。”她也有类似的恐惧感。

每当这些时候，我都想消除这种恐惧感，录个视频或者一篇小短文来介绍。一直没有动力。

# 初衷

看玉米大神的［独角兽］酷酷的，于是自己也动手建个类似的趣味项目。

想有意义些，不想做常见的互联网项目。于是，常常在思考该做点什么好。终于有一天，在跟一位回家的同学发消息时，脑电波搜寻到一个场景继而迸发了一个不错的点子：集合大家的力量教长辈们使用最新最好玩的科技好物，传授使用经验和技巧。

不管了，行动起来，再思考下去就变成“战术伟大”了。

# 起名

自己是个工科生，死理性派，想不起文绉绉的名，只留下看到“twitter”（叽叽喳喳）、“知乎”、“滴滴打车”这些产品名时暗自赞美的份。

今天在知乎上看到一位前辈的回答，觉得非常有用，颇有思路。

https://www.zhihu.com/question/20710616/answer/15930867

大前提是他提到的第3点，在这基础上再融入第1点的思想。

结合自己此前的思考，决定命名为：扬气吐眉

# 网站结构

主要板块：经验、问答、辟谣和应用推荐

首页：编辑推荐、最新文章（经验、辟谣、应用推荐）

# 数据库设计（TODO：字符图形表示）

用户表

经验、问答、辟谣和应用推荐各一个表
