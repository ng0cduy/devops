```
resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)
```

```
az vm deallocate --resource-group $resource_group --name xfusion-vm
```

```
az vm nic add --resource-group $resource_group --vm-name xfusion-vm --nics xfusion-
nic
```

```
az vm start --resource-group $resource_group --name xfusion-vm
```