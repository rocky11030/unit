# k8s的Job和CronJob控制器

myjob.yml文件说明
===========

+ completions表示完成6个容器
+ parallelism表示并行2个执行
+ restartPolicy为重启策略，Never从不重启，OnFailure为遇到失败重启

cronjob.yml文件说明
===========

+ kind为CronJob,定时任务的controller
+ schedule后面表示定时1分钟启动一次
