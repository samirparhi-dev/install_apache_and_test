def test_folders_exist_and_permissions(host):
    folders = [
        {"path": "/user/ache", "permissions": "0755"},
        {"path": "/var/www/html", "permissions": "0700"},
        {"path": "/tmp/myfolder", "permissions": "0777"},
    ]

    for folder in folders:
        folder_stat = host.file(folder["path"])
        assert folder_stat.exists, f"{folder['path']} does not exist"
        assert oct(folder_stat.mode) == f"0{folder['permissions']}", \
            f"{folder['path']} has incorrect permissions: {oct(folder_stat.mode)}"