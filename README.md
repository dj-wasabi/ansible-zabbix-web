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

#Overview

Build Status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-zabbix-server.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-zabbix-server)

This is an role for installing and maintaining the zabbix-server.

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-web (https://galaxy.ansible.com/dj-wasabi/zabbix-server/)
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

See the following list of supported Operating systems with the Zabbix releases:

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

#Installation

Installing this role is very simple: `ansible-galaxy install dj-wasabi.zabbix-web`

#Role Variables

## Main variables
There are some variables in de default/main.yml which can (Or needs to) be changed/overriden:


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


For more information, please check the following page: https://wdijkerman.wordpress.com/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker


# License

GPLv3

# Author Information

Github: https://github.com/dj-wasabi/ansible-zabbix-web

mail: ikben [ at ] werner-dijkerman . nl
