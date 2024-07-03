# This manifest uses the exec Puppet resource to kill a process named killmenow using pkill

exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin', '/usr/local/bin'],
  refreshonly => false,
}
