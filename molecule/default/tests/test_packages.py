"""Test for packages."""
import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("filebeat", "6.2.3"),
])
def test_package_ver(host, name, version):
    """Test package version."""
    assert host.package(name).is_installed
    assert host.package(name).version.startswith(version)
