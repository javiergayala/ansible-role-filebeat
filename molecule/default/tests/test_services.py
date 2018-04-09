"""Test for services."""
import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "filebeat"
])
def test_services(host, name):
    """Test that service is running and enabled."""
    s = host.service(name)
    assert s.is_running
    assert s.is_enabled
