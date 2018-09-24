# navigation 导航页

脚本说明
========

+ 系统环境: linux
+ 使用的web环境: Nginx 
+ 主要的步骤是: 上传到gitlab上面navigation代码，然后部署代码的服务器定期下载gitlab代码，重新nginx; 这样就完成了更新的操作
+ 更新的操作主要是: navication里面的index.html页
+ 里面包含了nginx.conf和default的配置，其中default在/etc/nginx/sites-enabled下面

> 使用crontab定时下载代码
``` bash
# crontab -e
*/1 * * * * cd /home/ubuntu/navigation && /usr/bin/git pull origin master:master
*/5 * * * * sudo service nginx reload
```

