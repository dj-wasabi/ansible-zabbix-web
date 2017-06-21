import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("server, redhat, debian", (
        ("zabbix-server-pgsql", "zabbix-web-pgsql", "zabbix-frontend-php"),
        ("zabbix-server-mysql", "zabbix-web-mysql", "zabbix-frontend-php"),
))
def test_zabbix_package(Package, TestinfraBackend, server, redhat, debian, SystemInfo):
    host = TestinfraBackend.get_hostname()
    host = host.replace("-centos", "")
    host = host.replace("-debian", "")
    host = host.replace("-ubuntu", "")

    if host == server:
        if SystemInfo.distribution in ['debian', 'ubuntu']:
            zabbix_web = Package(debian)
            assert zabbix_web.version.startswith("1:3.2")
        elif SystemInfo.distribution == 'centos':
            zabbix_web = Package(redhat)
            assert zabbix_web.version.startswith("3.2")
        assert zabbix_web.is_installed


def test_zabbix_web(File, SystemInfo):
    zabbix_web = File("/etc/zabbix/web/zabbix.conf.php")

    if SystemInfo.distribution in ['debian', 'ubuntu']:
        assert zabbix_web.user == "www-data"
        assert zabbix_web.group == "www-data"
    elif SystemInfo.distribution == 'centos':
        assert zabbix_web.user == "apache"
        assert zabbix_web.group == "apache"
    assert zabbix_web.mode == 0o644
