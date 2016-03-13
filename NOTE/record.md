 #TODO

* templates 的问题：extends base.html

* 




#问题

##2016-2-16: MySQL
尝试在项目中使用MySQL

使用homebrew顺利安装。但是在启动MySQL服务时遇到问题，使用mysql －u命令尝试登录时一直提示找不到sock
而对mysql不了解的我，完全不知道这是怎么一回事。
在网上查了一番，seagmentfault上一个问答里，发现使用brew命令也可以启动mysql，也下载了XAMPP。

第二天，开电脑后发现，使用mysql －u 命令可以正常登录。真是奇怪。不知道是重启了才使其服务运行起来，还是XAMPP带来的效果。

##2016-2-18: MySQL
MySQL建表时发现极度缺乏相关知识，只知道对应列应该用何种数据类型、长度等因素
是否该为NULL这个方面的了解则不够深，没有透彻地了解NULL其目的、如何应用


##2016-3-1: 今天待解决问题
mysql建表
tornado的登录功能（实现登录后登录注册按钮消失）

##2016-3-5: MySQL
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

## 2016-3-6: torndb

sudo pip install torndb 之后
在ipython里测试 import torndb 报错，No module named MySQLdb
Google之后在stackoverflow查到：sudo pip install mysql-python 之后再去ipython测试，正常。
