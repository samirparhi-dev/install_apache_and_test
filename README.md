## 🚀 To Run This Role:

```
ansible-playbook -i tests/inventory/hosts.yml playbook.yml
```

## ⚙️ Run with Galaxy :

```
ansible-galaxy install -r requirements.yml
```
## ⑇ What about test ?

Don Worry Here it is :

### Run with pytest-ansible:

```
pytest tests/
```

### Molecule Tests (WIP):

```
pip install molecule[docker] pytest testinfra
```
then run :

```
molecule test
```



