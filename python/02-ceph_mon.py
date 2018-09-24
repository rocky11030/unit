#!-*- coding:utf8 -*-

import requests
import time
import json
import commands

cephCmd = "ceph -s"
status, output = commands.getstatusoutput(cephCmd)
if status != 0:
    print("Get Ceph Status Failed!")

#cephStatus = "Failed"
cephStatus = "0"
if "HEALTH_OK" in output:
#    cephStatus = "OK"
    cephStatus = "1"

#cephTag = "cephStatus=" + cephStatus

ts = int(time.time())
payload = [
    {
        "endpoint": "10.2.29.2",
        "metric": "ceph-status",
        "timestamp": ts,
        "step": 60,
        #"value": 2,
        "value": cephStatus,
        "counterType": "GAUGE",
        #"tags": cephTag,
        "tags": "",
    },
]

r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

print r.text
