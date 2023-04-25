# Install Nginx server, setup and configuration with Puppet

package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'location \/redirect_me{\n\t\treturn 301 http:\/\/www.google.com;}',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
