# 0x0A. Configuration Management

## DevOps
## SysAdmin
## Scripting
## CI/CD

### Requirements
**General**
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp

**Note on Versioning**
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
```sh
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
