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
  content => 'Hello World!',
  require => File['/var/www/html'],
  notify  => Service['nginx'],
}

# Ensure the Nginx configuration is valid and reload Nginx
exec { 'nginx-reload':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
