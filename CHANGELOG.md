#ansible-zabbix-web Release

Below an overview of all changes in the releases.

Version (Release date)

1.2.0   (2018-09-11)

  * Updated supported versions #27
  * Readme lang typos grammar #28 (By pull request: dnmvisser (Thanks!))
  * Reflect license change to MIT in README #29 (By pull request: stephankn (Thanks!))
  * Fix for #24 #30
  * Fix for: SSLPassPhraseDialog setting problems - /usr/libexec/httpd-ss… #31

1.1.0   (2018-06-23)

  * added support for HTTPS #25 (By pull request: q1x (Thanks!))
  * Make debian 9 work #22
  * Updated minimal Ansible version to 2.4 #21
  * Changed version_compare operator to avoid deprecation warnings #19 (By pull request: nidr0x (Thanks!))
  * Most of the time php behaves better with leading semicolon. #17 (By pull request: toke (Thanks!))
  * add php7.0-gd #16 (By pull request: scil (Thanks!))
  * Fixed missing attribute iteritems #15 (By pull request: toke (Thanks!))
  * Allow usage of php environment variables #13 (By pull request: toke (Thanks!))
  * Make use of Molecule V2
  * Add support for debian stretch #7 (By pull request: dulin (Thanks!))
  * Fix Zabbix graph legend bug for Debian packages (see ZBX-10467) #6 (By pull request: mgornikov (Thanks!))
  * Split zabbix_url and Apache vhost ServerName #5 (By pull request: eshikhov (Thanks!))

1.0.0   (2017-08-30)

  * Removed tags 'always' on few tasks.
  * Fix for: Installing Zabbix-Web-MySQL Failed #1

0.1.0   (2017-06-16)

  * Initial working version.
