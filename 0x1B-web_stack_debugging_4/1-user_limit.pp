#Enable the user holberton to login

#increase hardlimit for holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

#increase soft file limit for holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command  => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}
