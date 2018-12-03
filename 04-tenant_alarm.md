# tenant_alarm.py

使用说明
========

- 此项目主要是使用python连接数据库，并查询数据过滤几个月内租户的到期时间，month=0为1个月内，month=1为2个月，month=2为3个月
- 又加了之前过期的租户日期打印，通过PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) <12 and PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) >=0,然后使用OR连接2个月后的日期打印出来
- 使用数据库查询的内容(返回的results)拼接成邮件的正文,并使用return把all_info正文的信息返回
- 最后smtplib模块发送邮件
- 此实例主要使用了函数def
- 此实例增加了保存excel和发送的功能


功能1: 返回results
--------------
* 具体代码如下
```
conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(get_info)
    results = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return results
```
功能2: 返回all_info
--------------
* 具体代码如下
```
all_info = ""
    for item in results:
        all_info += '租户名称：' + item[1].encode('utf-8') + '\n' + '登录名称: ' + item[3].encode('utf-8')+ '\n' + '到期时间：' + item[2].strftime(
            '%Y-%m-%d %H-%M-%S') + '\n' + '租户备注：' + item[0].encode('utf-8') + '\n\n'
    return all_inf
```
