# k8s的deployment控制器

yml文件说明
===========

+ apiVersion是当前配置格式的版本
+ kind是要创建的资源类型，这里是Deployment
+ metadata是该资源的元数据，name是必需的元数据项
+ spec部分是该Deplyment的规格说明
+ replicas 指明副本的数量，默认为1
+ template定义pod的模板，这是配置文件的重要部分
+ metadata定义pod的元数据，至少要定义一个label，label的key和value可以任意指定
+ spec描述pod的规格，此部分定义pod中每一个容器的属性，name和image是必需的

第一步: 应用yaml文件
--------------
* kubectl apply -f nginx.yml 

第二步: 删除deployment
--------------
* kubectl delete -f nginx.yml

第三步: 修改deployment
--------------
* 修改nginx.yml的副本数
* kubectl apply -f nginx.yml
