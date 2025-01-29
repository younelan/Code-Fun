apt-get update

if ! [ -L /var/www ]; then
    rm -rf /var/www
    ln -fs /vagrant/www /var/www
fi

sudo apt-get install -y nginx
sudo apt-get install -y php7.0 php7.0-fpm php7.0-cli php7.0-common php7.0-mbstring php7.0-gd php7.0-intl php7.0-xml php7.0-mysql php7.0-mcrypt php7.0-zip

#/vi /etc/php/7.0/fmp/php.ini
systemctl restart nginx.service php7.0-fpm.service

apt install mysql-server
sudo apt-get install postgresql
sudo apt install postgresql-contrib

cat << 'EOF' > /etc/nginx/sites-available/default
server {
	# Port that the web server will listen on.
	listen 80;

	# Host that will serve this project.
	server_name localhost;

	# Useful logs for debug.
	access_log /var/log/nginx/localhost_access.log;
	error_log /var/log/nginx/localhost_error.log;
	rewrite_log on;

	# The location of our projects public directory.
	root /usr/share/nginx/html;

	# Point index to the Laravel front controller.
	index index.php index.html;

	location / {
		# URLs to attempt, including pretty ones.
		try_files $uri $uri/ /index.php?$query_string;
	}

	# Remove trailing slash to please routing system.
	if (!-d $request_filename) {
		rewrite ^/(.+)/$ /$1 permanent;
	}

	# PHP FPM configuration.
	location ~* \.php$ {
		fastcgi_pass unix:/run/php/php7.1-fpm.sock;
		fastcgi_index index.php;
		fastcgi_split_path_info ^(.+\.php)(.*)$;
		include /etc/nginx/fastcgi_params;
		fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
	}

	# We don't need .ht files with nginx.
	location ~ /\.ht {
		deny all;
	}

	# Set header expirations on per-project basis
	location ~* \.(?:ico|css|js|jpe?g|JPG|png|svg|woff)$ {
		expires 365d;
	}
}
EOF

# Restart servers
service nginx restart
service php7.1-fpm restart

