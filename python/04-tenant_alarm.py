# -*- coding: utf-8 -*-

import smtplib
import mysql.connector
from email.mime.text import MIMEText
from email.header import Header

config={'host':'10.2.80.2',
        'user':'root',
        'password':'********',
        'port':3306 ,
        'database':'AuthCenter',
        'charset':'utf8'}

def get_tenant(months):#获取租户信息
    get_info ="SELECT description,`name`,end_date,email  FROM tenant WHERE PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) <1 and PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) >=-"+str(months)+" AND TO_DAYS( NOW( ) ) - TO_DAYS( end_date) < 0"
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(get_info)
    results = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return results

def email_content(results):#整理邮件内容
    all_info = ""
    for item in results:
        all_info += '租户名称：' + item[1].encode('utf-8') + '\n' + '登录名称: ' + item[3].encode('utf-8')+ '\n' + '到期时间：' + item[2].strftime(
            '%Y-%m-%d %H-%M-%S') + '\n' + '租户备注：' + item[0].encode('utf-8') + '\n\n'
    return all_info

def send_email(receivers,all_info):
    mail_host = "smtp.exmail.qq.com"  # SMTP服务器
    mail_user = "cloud_service@neunn.com"  # 用户名
    mail_pass = "******"  # 登录密码

    sender = 'cloud_service@neunn.com'  # 发件人邮箱(最好写全, 不然会失败)
    message = MIMEText(all_info, 'plain', 'utf-8')
    message['From'] =  "{}".format(sender)
    message['To'] = Header("各位同事", 'utf-8')
    subject = '租户到期提醒'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException,e:
        print "Error: 无法发送邮件"
        print e

def main():
    months = 1#设置获取信息月份，当前月份为0，下一个月为1，
    receivers = ['****@126.com','****@163.com']  # 接收邮箱
    results = get_tenant(months)#获取租户信息
    all_info = email_content(results)#整理邮件内容
    send_email(receivers,all_info)#发送邮件

if __name__ == '__main__':

main()
