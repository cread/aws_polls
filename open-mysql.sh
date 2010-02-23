#!/bin/bash

WHOAMI=`/usr/bin/whoami`

if [ "${WHOAMI}" != "root" ]; then
    echo "This script needs to run as root. You are trying to run it as ${WHOAMI}"
    exit 1
fi

if [ ! -x /usr/bin/mysql ]; then
    echo "Can't find mysql executable at '/usr/bin/mysql'"
    exit 2
fi

echo "GRANT ALL ON aws_polls.* TO 'aws_polls'@'%' IDENTIFIED BY 'awspolls';" | /usr/bin/mysql mysql

echo "[mysqld]" > /etc/mysql/conf.d/aws_polls.cnf
echo "bind-address = 0.0.0.0" >> /etc/mysql/conf.d/aws_polls.cnf

/etc/init.d/mysql restart


