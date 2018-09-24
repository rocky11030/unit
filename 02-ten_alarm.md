# ten_vm.sql

语句说明
========

+ 数据库环境: Mysql5.5
+ 语句功能主要是查询end_date到期时间，主要是从今天到月底和(下个月或者大下个月)的到期租户
+ period_diff 显示月份的不同,用前面的参数减去后面的参数
+ 现在的时间-end_date的时间<1，表示过滤掉上个月以前的end_date
+ 现在的时间-end_date的时间>=-1,表示要这个月和下个月的时间,也可以使用-2来表示这个月、下个月和大下个月的时间 
+ TO_DAYS返回一个从公元0年到现在的天数

> 使用
``` bash
# service crond restart (centos) or service cron restart (ubuntu)
```

