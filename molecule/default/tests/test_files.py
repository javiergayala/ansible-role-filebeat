"""Test for files."""
import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name, content", [
    ('/etc/yum.repos.d/elasticsearch-6.x.repo',
     'baseurl = https://artifacts.elastic.co/packages/6.x/yum'),
    ('/etc/filebeat/filebeat.yml',
     'filebeat.config.modules:'),
    ('/etc/filebeat/filebeat.yml',
     'filebeat.prospectors:'),
    ('/etc/filebeat/filebeat.yml',
     'output.elasticsearch:'),
    ('/etc/filebeat/filebeat.yml',
     'setup.template.settings:'),
    ('/etc/filebeat/modules.d/system.yml',
     'syslog:'),
    ('/etc/filebeat/filebeat.yml',
     'system: true'),
])
def test_files(host, name, content):
    """Test that file exists."""
    f = host.file(name)
    assert f.exists
    assert f.is_file
    assert f.contains(content)
