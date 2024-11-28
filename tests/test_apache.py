def test_apache_installed(ansible_module):
    result = ansible_module.yum(name="httpd", state="present")
    assert result['changed'] is False  # Apache should already be installed
    assert result['rc'] == 0

def test_apache_service_running(ansible_module):
    result = ansible_module.service(name="httpd", state="started")
    assert result['changed'] is False  # Apache should already be running
    assert result['rc'] == 0

def test_check_folders_called(ansible_module):
    result = ansible_module.stat(path="/user/ache")
    assert result['stat']['exists'] is True  # Folder should exist
    assert result['stat']['mode'] == '0755'  # Folder should have correct permissions

def test_install_tar_called(ansible_module):
    result = ansible_module.stat(path="/opt/sample")
    assert result['stat']['exists'] is True  # TAR should be extracted
