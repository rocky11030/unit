# 自动缩容ceph脚本

脚本说明
========

+ 测试成功系统环境: ubuntu14.04
+ 使用os、commands、time和pdb等模块
+ 使用pdb来测试python，n为下一步，c为执行，中间可以用print来测试输出的变量
+ 使用split("\n")把awk获取的id转为python的列表格式
+ 通过for循环里面使用while True，在while True里面使用条件，满足条件后跳出。这样每次删除osd后再平衡后，再进行下次循环

第一步: 注释掉pdb执行
--------------
``` bash
#import pdb; pdb.set_trace()
```
* 执行脚本: python 01-reduce.py

第二步: 直接执行
--------------
* 执行脚本: python 01-reduce.py
* n为下一步，c为执行
