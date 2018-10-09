# k8s的pv和pvc

脚本说明
===========

+ 首先在master节点创建一个NFS server，共享文件夹为/nfsdata/pv1
+ 然后再其他的所有k8s节点上需要安装NFS客户端，因为是ubuntu系统，使用apt-get install nfs-common -y
+ 执行顺序为kubectl apply -f 05-nfs-pv1.yml && kubectl apply -f 05-nfs-pvc1.yml && kubectl -f 05-pod1.yml 
+ 使用kubectl exec mypod1 touch /mydata/hello,然后验证主节点的ls /nfsdata/pv1/里面是否有hello即可 

05-nfs-pv1.yml文件说明
===========

+ ReadWriteOnce为指定的访问模式，ReadWriteOnce – PV 能以 read-write 模式 mount 到单个节点，ReadOnlyMany – PV 能以 read-only 模式 mount 到多个节点，ReadWriteMany – PV 能以 read-write 模式 mount 到多个节点。
+ Recycle为PV的回收策略,Retain – 需要管理员手工回收，Recycle – 清除 PV 中的数据，效果相当于执行 rm -rf /thevolume/*，Delete – 删除 Storage Provider 上的对应存储资源

05-nfs-pvc1.yml文件说明
===========

+ 创建一个PVC,只需要指定pv的容量、访问模式和class即可

05-pod1.yml文件说明
===========

+ 创建一个POD，与使用普通 Volume 的格式类似，在 volumes 中通过 persistentVolumeClaim 指定使用 mypvc1 申请的 Volume。
