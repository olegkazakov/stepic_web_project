#nginx conf
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo rm /etc/nginx/sites-enabled/default
fi

touch /home/box/nginx.log
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#gunicorn conf
touch /home/box/gunicorn.log
#sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

sudo service mysql restart
mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8 COLLATE utf8_general_ci"
mysql -uroot -e "CREATE USER 'ok_ask'@'localhost' IDENTIFIED BY 'ok_ask'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'ok_ask'@'localhost'"

python /home/box/web/ask/manage.py syncdb
#remove /etc/gunicorn.d/ask before run
#python /home/box/web/ask/manage.py runserver 0.0.0.0:8000 &
