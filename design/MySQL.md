# 2016-12-21
新建用户表：
create table user(
id int not NULL auto_increment,
username varchar(16) not NULL,
password varchar(16) not NULL,
email varchar(32) not NULL,
regtime datetime not NULL,
PRIMARY KEY (id)
);

用户ID改成从某个数开始自增：
alter table user auto_increment=1000;

注册时间在后端实现：
insert into user(username, password, email, regtime) values("wujian", "abc123", "wujian@github.com", curtime());



# 2017-01-03 星期二
摘要：为第一版做最后的优化。

用户表：
ID
用户名
密码
邮箱
注册时间

投递表：
create table post(
id int not NULL auto_increment,
title varchar(32) not NULL,
author varchar(16) not NULL,
text text not NULL,
posttime datetime not NULL,
tag varchar(16) not NULL,
PRIMARY KEY (id)
);

alter table post auto_increment=1000;

投递post表里，tag的思考：
出于方便存储、方便前端使用的考虑，决定每篇文章只定一个tag。这样可以直接存储，省下工作量，可以快速上线，
前端投稿时做限制，只能选一个标签tag。搜索时，则可以直接在数据库查询关键字。
后期如果有更强大的需求可以再优化此处。
搜索还可以用这个：
select title from article where text like "%微信%";

## 需要在前端限制标题长度、文章长度
