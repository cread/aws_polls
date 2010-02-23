#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 <db username> <db password> <db host>"
    exit 1
else
    echo "DATABASE_USER = '$1'"
    echo "DATABASE_PASSWORD = '$2'"
    echo "DATABASE_HOST = '$3'"
fi

aptitude update
aptitude -y safe-upgrade
aptitude -y install libpython2.6 python-django python-mysqldb libapache2-mod-wsgi

cd /var/tmp
wget -O aws_polls.tar.gz http://github.com/cread/aws_polls/tarball/master
tar fxz aws_polls.tar.gz
mv cread-aws_polls-* aws_polls
cd aws_polls

echo "DATABASE_USER = '$1'" >> settings.py
echo "DATABASE_PASSWORD = '$2'" >> settings.py
echo "DATABASE_HOST = '$3'" >> settings.py

/usr/bin/python manage.py syncdb

cp aws_polls.apache /etc/apache2/sites-available/aws_polls

a2dissite default
a2ensite aws_polls

/etc/init.d/apache2 reload

