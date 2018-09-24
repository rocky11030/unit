#!-*- coding:utf8 -*-
import commands
import os
#import sys
import time
#使用pdb来测试python，n为下一步，c为执行，中间可以用print来测试输出的变量
import pdb; pdb.set_trace()
ids = commands.getoutput("ls /var/lib/ceph/osd | awk -F-  '{print $2}'").split("\n")
for osdid in ids:    
    os.system("stop ceph-osd id=%s" %osdid)
    os.system("ceph osd out osd.%s" %osdid)
    os.system("ceph osd crush remove osd.%s" %osdid)
    os.system("ceph osd rm osd.%s" %osdid)

    while True:
        time.sleep(10)
        output = commands.getoutput("ceph -s")
        if "HEALTH_OK" in output:
            break
status,output = commands.getstatusoutput("ps -ef|grep osd | grep -v grep")
hostname =  commands.getoutput("hostname")
if status !=0:
    os.system("ceph osd crush remove %s" %hostname)
