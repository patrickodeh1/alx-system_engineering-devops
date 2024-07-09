#puppet for ssh config
file_line { 'Turn off passwd auth':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
    match => '^#?PasswordAuthentification',
}

file_line { 'Turn off passwd auth':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
    match => '^#?IdentityFile',
}
