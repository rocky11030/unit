# 批量启动容器脚本

脚本说明
========

+ 测试成功系统环境: ubuntu16.04
+ 安装python-pip，通过pip安装docker-py,执行ansible的docker_container模块必须要安装docker-py
+ 通过register，获取到所有exited的容器id的变量resulst
+ 通过resulst.stdout_lines输出容器id启动容器

第一步: 解决ubuntu16.04不支持python2.7的问题
--------------
* 使用ansible推送python到目标ubuntu16.04主机
``` bash
# ansible -i hosts container --sudo -m raw -a "apt install -y python-minimal python-simplejson"
```
* 安装后,在目标主机使用which python 和 python -V 后发现，Python版本为2.7.12

第二步: 启动停止的容器
--------------
* 执行脚本:ansible-playbook -i hosts start_container.yml
* 执行开始模块可以添加tag start
