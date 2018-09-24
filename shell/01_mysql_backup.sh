#!/bin/bash

BAKDIR=/data/mysqlbackup/`date +%Y_%m_%d`
#which mysql
MYCMD=/data/mysql/bin/mysqldump
MYSQLDB=zs_smartrouter
MYSQLUSER=root
MYSQLPW=rootLink
DAYS=30

#To determine whether the user is root
if 
  [ $UID -ne 0 ]; then
  echo "This script must be the root user"
  sleep 2
  exit 0
fi

#judge folder
if
 [ ! -d $BAKDIR ]; then
 mkdir $BAKDIR
 echo "$BAKDIR is create successfully!"
 else
 echo "this backdir is exit..."
fi

$MYCMD -u$MYSQLUSER -p$MYSQLPW $MYSQLDB > $BAKDIR/$MYSQLDB.sql

#judge success
if [ $? -eq 0 ]; then
   echo "This backup mysql database is successfully!"
else
   echo "This backup mysql database is failed"
fi

#compress database
cd $BAKDIR
tar -zcf $MYSQLDB.tar.gz $MYSQLDB.sql && rm -rf $MYSQLDB.sql
#retain time is 30 days
find $BAKDIR -type d -mtime +$DAYS -exec rm -rf {} \;


