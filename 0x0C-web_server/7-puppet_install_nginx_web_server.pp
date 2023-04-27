# Configure a server including a redirect page using puppet instead of bash

# Add nginx package to repo
exec { 'add nginx stable repo':
  command => 'sudo apt-get-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

# Update packages
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

# Install nginx package
exec { 'nginx':
  ensure => 'installed'
}

# Firewall config
exec { 'allow HTTP':
  command => 'ufw allow "Nginx HTTP"',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1'
}

# Folder privileges
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

# Index file for site
file { '/var/www/html/index.html':
  content => 'Hello World!\n'
}

# 'File not found' file (error 404)
file { '/var/www/html/error404.html':
  content => "Ceci n'est pas une page\n"
}

# Include redirection and error page to server configuration
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
    "server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html index.htm index.nginx-debian.html;
      server_name _;
      location / {
          try_files \$uri \$uri/ =404;
      }

      error_page 404 /error404.html;
      location = /error404.html {
          internal;
      }

      if (\$request_filename ~ redirect_me) {
          rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
      }
    }"
}

# Restart nginx service
exec { 'restart service':
  command => 'sudo service nginx restart'.
  path    => '/usr/bin:/usr/sbin:/bin'
}

# Start nginx service
exec { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
