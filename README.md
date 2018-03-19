Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
  - [Operating systems](#operating-systems)
  - [Zabbix Versions](#zabbix-versions)
    - [Zabbix 3.2](#zabbix-32)
    - [Zabbix 3.0](#zabbix-30)
    - [Zabbix 2.4](#zabbix-24)
    - [Zabbix 2.2](#zabbix-22)
- [Installation](#installation)
- [Role Variables](#role-variables)
  - [Main variables](#main-variables)
- [Dependencies](#dependencies)
- [Example Playbook](#example-playbook)
  - [Single instance](#single-instance)
  - [Multi host setup](#multi-host-setup)
- [Molecule](#molecule)
- [License](#license)
- [Author Information](#author-information)

# Overview

Build Status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-zabbix-web.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-zabbix-web)

This is a role for installing and maintaining the zabbix-web, the web UI for the zabbix-server.

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-web (https://galaxy.ansible.com/dj-wasabi/zabbix-web/)
 * zabbix-server (https://galaxy.ansible.com/dj-wasabi/zabbix-server/)
 * zabbix-proxy (https://galaxy.ansible.com/dj-wasabi/zabbix-proxy/)
 * zabbix-javagateway (https://galaxy.ansible.com/dj-wasabi/zabbix-javagateway/)
 * zabbix-agent (https://galaxy.ansible.com/dj-wasabi/zabbix-agent/)

# Requirements
## Operating systems

This role will work on the following operating systems:

 * Red Hat
 * Debian
 * Ubuntu

So, you'll need one of those operating systems.. :-)
Please sent Pull Requests or suggestions when you want to use this role for other Operating systems.

## Zabbix Versions

See the following list of supported Operating systems with the Zabbix releases.

### Zabbix 3.2

  * CentOS 7.x
  * Amazon 7.x
  * RedHat 7.x
  * OracleLinux 7.x
  * Scientific Linux 7.x
  * Ubuntu 14.04, 16.04
  * Debian 7, 8

### Zabbix 3.0

  * CentOS 5.x, 6.x, 7.x
  * Amazon 5.x, 6.x, 7.x
  * RedHat 5.x, 6.x, 7.x
  * OracleLinux 5.x, 6.x, 7.x
  * Scientific Linux 5.x, 6.x, 7.x
  * Ubuntu 14.04
  * Debian 7, 8

### Zabbix 2.4

  * CentOS 6.x, 7.x
  * Amazon 6.x, 7.x
  * RedHat 6.x, 7.x
  * OracleLinux 6.x, 7.x
  * Scientific Linux 6.x, 7.x
  * Ubuntu 12.04 14.04
  * Debian 7

### Zabbix 2.2

  * CentOS 5.x, 6.x
  * RedHat 5.x, 6.x
  * OracleLinux 5.x, 6.x
  * Scientific Linux 5.x, 6.x
  * Ubuntu 12.04
  * Debian 7
  * xenserver 6

# Installation

Installing this role is very simple: `ansible-galaxy install dj-wasabi.zabbix-web`

When the Zabbix Web needs to be running on the same host as the Zabbix Server, please also install the Zabbix Server by executing the following command: `ansible-galaxy install dj-wasabi.zabbix-server`

# Role Variables

## Main variables

The following is an overview of all available configuration default for this role.

### Overall Zabbix

* `zabbix_version`: This is the version of zabbix. Default: 3.2. Can be overridden to 2.0, 2.4, 2.2 or 2.0.
* `zabbix_repo_yum`: A list with Yum repository configuration.

### Zabbix Web specific

* `zabbix_url`: This is the url on which the zabbix web interface is available. Default is zabbix.example.com, you should override it. For example, see "Example Playbook"
* `zabbix_url_aliases`: A list with Aliases for the Apache Virtual Host configuration.
* `zabbix_timezone`: This is the timezone. The Apache Virtual Host needs this parameter. Default: Europe/Amsterdam
* `zabbix_vhost`: True / False. When you don't want to create an Apache Virtual Host configuration, you can set it to False.
* `zabbix_apache_vhost_port`: On which port the Apache Virtual Host is available.
* `zabbix_web_max_execution_time`:
* `zabbix_web_memory_limit`:
* `zabbix_web_post_max_size`:
* `zabbix_web_upload_max_filesize`:
* `zabbix_web_max_input_time`:
* `zabbix_web_env`: A Dictionary of PHP Environments

### Zabbix Server

* `zabbix_server_name`: The name of the Zabbix Server.
* `zabbix_server_database`: The type of database used. Can be: mysql or pgsql
* `zabbix_server_database_long`: The type of database used, but long name. Can be: mysql or postgresql
* `zabbix_server_hostname`: The hostname on which the zabbix-server is running. Default set to: {{ inventory_hostname }}
* `zabbix_server_listenport`: On which port the Zabbix Server is available. Default: 10051
* `zabbix_server_dbhost`: The hostname on which the database is running.
* `zabbix_server_dbname`: The database name which is used by the Zabbix Server.
* `zabbix_server_dbuser`: The database username which is used by the Zabbix Server.
* `zabbix_server_dbpassword`: The database user password which is used by the Zabbix Server.
* `zabbix_server_dbport`: The database port which is used by the Zabbix Server.

## Examples of configuration

### zabbix_repo_yum

Current default configuration and example for  

````
zabbix_repo_yum:
  - name: zabbix
    description: Zabbix Official Repository - $basearch
    baseurl: http://repo.zabbix.com/zabbix/{{ zabbix_version }}/rhel/{{ ansible_distribution_major_version }}/$basearch/
    gpgcheck: 0
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX
    state: present
  - name: zabbix
    description: Zabbix Official Repository non-supported - $basearch
    baseurl: http://repo.zabbix.com/non-supported/rhel/{{ ansible_distribution_major_version }}/$basearch/
    gpgcheck: 0
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX
    state: present
````

# Dependencies

This role has 1 "hardcoded" dependency: geerlingguy.apache.

As it is also possible to run the zabbix-web on a different host than the zabbix-server, the zabbix-server is not configured to be an dependency.

# Example Playbook

There are 2 ways for using the zabbix-web:

* Single instance
* Multi host setup

## Single instance

When there is one host running both Zabbix Server and the Zabbix Web (Running MySQL as database):

```
- hosts: zabbix-server
  become: yes
  roles:
     - { role: geerlingguy.apache }
     - { role: dj-wasabi.zabbix-server, database_type: mysql, database_type_long: mysql, server_dbport: 3306 }
     - { role: dj-wasabi.zabbix-web, zabbix_url: zabbix.dj-wasabi.nl, database_type: mysql, database_type_long: mysql, server_dbport: 3306 }
```

## Multi host setup

This is a 2 host setup. On 1 host (Named: zabbix-server)the Zabbix Server is running and 1 host (Named: zabbix-web) where the Zabbix Web is running (Running MySQL as database):

```
- hosts: zabbix-server
  become: yes
  roles:
     - { role: dj-wasabi.zabbix-server, database_type: mysql, database_type_long: mysql, server_dbport: 3306 }

- hosts: zabbix-web
  become: yes
  roles:
     - { role: geerlingguy.apache }
     - { role: dj-wasabi.zabbix-web, zabbix_server_hostname: zabbix-server, zabbix_url: zabbix.dj-wasabi.nl, database_type: mysql, database_type_long: mysql, server_dbport: 3306 }
```

# Molecule

This role is configured to be tested with Molecule. Molecule will boot at least 3 different kind of containers, each of the supported Operating System (Debian, Ubuntu and Red Hat).
Pull Requests are only merged when the tests are succeeding.

For more information, please check the following page: https://www.werner-dijkerman.nl/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker

# License

GPLv3

# Author Information

Github: https://github.com/dj-wasabi/ansible-zabbix-web

mail: ikben [ at ] werner-dijkerman . nl
