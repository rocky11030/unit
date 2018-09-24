# ceph_mon.py

使用说明
========

- 此项目主要是使用监控ceph状态是否正常的脚本
- 通过post方法传给open-falcon的agent客户端


功能1: 判断HEALTH_OK是否在ceph -s的输出命令中
--------------
* 通过commands.getstatusoutput来获得ceph -s的状态和命令
* 判断是否在outpu中
```
    if "HEALTH_OK" in output:
        cephStatus = "1"
```
功能2: 回传value值给agent
--------------
* 通过endpoint机器名，metric属性和tags(这里赋值为空)返回给open-falcon
* step为返回间隔60秒，value使用变量cephStatus的返回值
* 最后打印返回成功print r.text
