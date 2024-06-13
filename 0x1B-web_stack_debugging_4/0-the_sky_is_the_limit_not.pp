# Increase the amount of traffic on nginx

#Increase the ulimit
exec { 'fix--for-nginx':
 #modify
 command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
 #specify path
 path    => '/usr/local/bin/:/bin/',
}
#restart nginx
exec { 'nginx-restart':
 #restart nginx service
 command => '/etc/init.d/nginx restart',
 #modify the path
 path   => '/etc/init.d/',
}

