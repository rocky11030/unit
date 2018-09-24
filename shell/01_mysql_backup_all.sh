#!/bin/bash

BAKDIR=/data/mysqlbackup/`date +%Y_%m_%d`
#which mysql
MYCMD=/usr/bin/mysqldump
MYSQLDB=--all-databases
all=all
MYSQLUSER=root
MYSQLPW=
ip=10.33.64.1
DAYS=15

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
 mkdir -p $BAKDIR
 echo "$BAKDIR is create successfully!"
 else
 echo "this backdir is exit..."
fi

$MYCMD -h $ip -u$MYSQLUSER -p$MYSQLPW $MYSQLDB > $BAKDIR/$all.sql

#judge success
if [ $? -eq 0 ]; then
   echo "This backup mysql database is successfully!"
else
   echo "This backup mysql database is failed"
fi

#compress database
cd $BAKDIR
tar -zcf $all.tar.gz $all.sql && rm -rf $all.sql
#retain time is 15 days
find $BAKDIR -type d -mtime +$DAYS -exec rm -rf {} \;


