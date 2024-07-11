# This Puppet manifest sets up Nginx with a custom HTTP header on a new Ubuntu server

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By $hostname;
    }
}",
  require => Package['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
}

