# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
}

# Configure the Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location = /redirect_me {
        return 301 http://$host;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
        root /var/www/html;
        index 404.html;
    }
}
  ',
  notify  => Service['nginx'],
}

# Ensure the content directory exists
file { '/var/www/html':
  ensure => directory,
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => File['/var/www/html'],
  notify  => Service['nginx'],
}

# Create a custom 404.html page
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => File['/var/www/html'],
  notify  => Service['nginx'],
}

# Ensure the Nginx configuration is valid and reload Nginx
exec { 'nginx-reload':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
