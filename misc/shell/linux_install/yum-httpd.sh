yum install -y httpd
#yum-config-manager --enable remi-php72
yum install -y postgresql-server postgresql-contrib 
yum install -y php php-pdo php-pecl-yaml php-fpm php-mysqlnd php-opcache
yum install -y php-xml php-xmlrpc php-gd php-mbstring php-json
yum install php-fpm php-intl php-pq

