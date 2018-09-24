# k8s的DaemonSet控制器

yml文件说明
===========

+ hostNetwork: true表示直接使用host网络
+ command设置容器的启动命令
+ volumeMounts为通过 Volume 将 Host 路径 /proc、/sys 和 / 映射到容器中 

第一步: 应用yaml文件
--------------
* kubectl apply -f node_exporter.yml 

第二步: 删除deployment
--------------
* kubectl delete -f node_exporter.yml

第三步: 查看部署后的pod
--------------
* kubectl get pod -o wide
