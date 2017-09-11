# various bash commands to setup environment
# TODO: create setup script or Docker Container that has these configurations
# Make it happen!

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install emacs
sudo apt-get install git
sudo pip3 install pep8
sudo apt-get install python3-pip3
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
sudo pip3 install sqlalchemy
sudo pip3 install flask
sudo pip3 install gunicorn
sudo wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
sudo sudo dpkg -i mysql-apt-config_0.6.0-1_all.deb
sudo apt-get update
sudo apt-get install mysql-server
rm -rf mysql-apt-config_0.6.0-1_all.deb
cat dev/100-dump.sql | mysql -uroot -p
sudo cp config/nginx.default /etc/nginx/sites-available/default
sudo cp config/airbnb* /etc/init/
sudo start airbnb
