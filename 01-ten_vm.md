# ten_vm.sql

语句说明
========

+ 数据库环境: Mysql5.5
+ 语句主要的作用查询租户和租户内虚机的详细配置信息，最后租户进行排序
+ as参数可以起别名
+ LEFT JOIN ...ON...为(左联接) 返回包括左表中的所有记录和右表中联结字段相等的记录
+ DATA_FORMAT为显示日期的格式
+ where的多个条件使用or,并用括号括起来
+ GROUP BY是分组的操作,因为uuid是唯一的可以用作去重复操作
+ ORDER BY可以用作排序操作

> 使用
``` bash
# service crond restart (centos) or service cron restart (ubuntu)
```

