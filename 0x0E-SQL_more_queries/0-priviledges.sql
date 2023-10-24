-- script that lists all privileges of the MySQL users user_0d_1 and 
-- user_0d_2 on your server (in localhost).
echo "SHOW GRANTS FOR 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
echo "SHOW GRANTS FOR 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p

