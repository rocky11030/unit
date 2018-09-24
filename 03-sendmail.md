# sendmail.py

使用说明
========

- 此项目主要是使用python发送邮件模块


功能1: 传输变量
--------------
* python sendmail.py test@163.com test 'test'
* 具体代码如下
```
    #objectFile = sys.argv[3]
    #mailObject = open(objectFile).read()
    #send_mail(mail_to,subject,mailObject)
    注释掉上面的代码
    send_mail(mail_to,subject,content)
```
功能2: 使用文件发送邮件
--------------
* python sendmail.py test@163.com test data.txt
* 具体代码如下
```
    objectFile = sys.argv[3]
    mailObject = open(objectFile).read()
    send_mail(mail_to,subject,mailObject)
    注释掉下面的代码
    #send_mail(mail_to,subject,content)
```
