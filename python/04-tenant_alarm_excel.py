# -*- coding: utf-8 -*-

import smtplib
import os
from datetime import datetime
import mysql.connector
import xlwt
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart #用MIMEMultipart()来构造实例

config={'host':'10.2.80.2',
        'user':'root',
        'password':'*******',
        'port':3306 ,
        'database':'AuthCenter',
        'charset':'utf8'}

def get_sql(sql):#获取数据库sql信息
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql)
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

def  deal_ten_info(results,xls_name):#写入Excel文档
    headers = [u'租户名称', u'登录名称',u'到期时间', u'租户备注']
    workbook = xlwt.Workbook()#新建一个excel文件
    sheet = workbook.add_sheet('table_tenant', cell_overwrite_ok=True)#新建一个sheet，第一个参数为sheet名称，第二参数用于确认同意cell单元是否可以重设值
    # 写上字段信息table.write(行，列，value)
    for i in range(len(headers)):
        sheet.write(0, i, headers[i])

        # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1, len(results) + 1):
        for col in range(0, 4):
            sheet.write(row, col, u'%s' % results[row - 1][col])
    workbook.save(xls_name) #保存文件

def send_email(receivers,all_info,exl_name):
    #发件人的信息
    mail_host = "smtp.exmail.qq.com"  # 第三方SMTP服务器
    mail_user = "cloud_service@neunn.com"  # 用户名
    mail_pass = "******"  # 登录密码
    sender = 'cloud_service@neunn.com'  # 发件人邮箱(最好写全, 不然会失败)


    msg = MIMEMultipart('alternative')
    message_text = MIMEText(all_info, 'plain', 'utf-8') #all_info为文本内容，plain设置文本格式，utf8设置编码
    msg.attach(message_text)
    msg['From'] = Header("租户到期", 'utf-8')
    #message['From'] =  "{}".format(sender)
    msg['To'] = Header("各位同事", 'utf-8')
    #邮件名称及格式
    subject = '租户到期提醒'
    msg['Subject'] = Header(subject, 'utf-8')

    att = MIMEText(open(exl_name, 'rb').read(), 'base64', 'utf-8') #exl_name为当先目录下的文件
    att['Content-type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename='+exl_name #这里的filename可以任意写，写什么名字，邮件里面就显示什么名字
    msg.attach(att)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  #连接第三方邮件服务器，25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass) #登录邮件服务器
        smtpObj.sendmail(sender, receivers, msg.as_string())#sender为发送者地址，receivers为接受者地址，message为发送消息
        print "邮件发送成功"
    except smtplib.SMTPException,e:
        print "Error: 无法发送邮件"
        print e

def remove_file(xls_name):
    if os.path.exists(xls_name):
        os.remove(xls_name)
        

def main():
    months = 1 #设置获取信息月份，当前月份为0，下一个月为1,大下个月为2，
    get_date ="SELECT description,`name`,end_date,email  FROM tenant WHERE PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) <12 and PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) >=0 OR  PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) >=-"+str(months)+" AND TO_DAYS( NOW( ) ) - TO_DAYS( end_date) < 0"
    get_info = "SELECT name as 租户名称,email as 登录名称,DATE_FORMAT(end_date,'%Y-%m-%d') as 到期时间,description as 租户备注 FROM tenant ORDER BY name"
    xls_name=str(datetime.now().strftime('%Y-%m-%d')) + ".xls"
    receivers = ['***@126.com','***@163.com']  # 接收邮箱
    end_date = get_sql(get_date) #获取租户信息
    all_info = email_content(end_date) #整理邮件内容
    get_ten = get_sql(get_info) #获取打印附件的信息
    deal_ten_info(get_ten,xls_name) #把数据库查询的内容保存成excel
    send_email(receivers,all_info,xls_name)#发送邮件
    remove_file(xls_name) #删除附件

if __name__ == '__main__':

    main()

