# mysql备份脚本

脚本说明
========

+ 系统环境: linux
+ 支持数据库: mysql or mariadb
+ 功能包括判断是否有root权限、是否有备份文件夹、备份数据库、判断是否备份成功、压缩删除未压缩数据和保留多少时间的备份
+ 参数: 备份目录=BAKDIR,备份命令=MYCMD,数据库名称=MYSQLDB,数据库用户名=MYSQLUSER,密码=MYSQLPW,保留时间=DAYS
+ 使用过程中需要修改各个参数
+ 包含两个脚本: 一个是备份单个数据库，另外一个是备份全库

> 使用crontab定时执行脚本
``` bash
# crontab -e
# 0 1 * * * root /bin/bash /data/mysqlbackup/mysql_backup.sh >> /tmp/mysql_backup.log 2>&1
# service crond restart (centos) or service cron restart (ubuntu)
```
>忽略备份openstack的垃圾数据
``` bash
$MYCMD -h $HOST -u$USER -p$PSWD $MYSQLDB \
 --ignore-table=keystone.token \
 --ignore-table=gnocchi.instance_history \
 --ignore-table=gnocchi.resource_history \
 --ignore-table=graph.endpoint_counter \
 --ignore-table=aodh.alarm_history > $BAKDIR/$MYSQLBAK.sql
```
