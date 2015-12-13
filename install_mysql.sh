sudo apt-get install mysql-server -y
sudo apt-get install mysql-client -y

#разрешить подключатся с любого хоста
echo --change: vi /etc/mysql/my.cnf.
echo bind-address            = 0.0.0.0
#разрешить подключатся только с указанного IP
echo bind-address            = 192.168.1.23
echo 
echo --Change default local to utf-8:
echo skip-character-set-client-handshake
echo character-set-server = utf8
echo init-connect='SET NAMES utf8'
echo collation-server=utf8_general_ci
echo
echo sudo service mysql restart
echo
echo --Check it:
echo mysql -u root -p123
echo SHOW VARIABLES LIKE 'char%';
echo
echo --create user:
echo CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
echo GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
echo FLUSH PRIVILEGES;
echo
echo CREATE DATABASE `django_db`;
#vi /etc/mysql/my.cnf.