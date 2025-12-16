```resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)```
```az vm disk attach --vm-name nautilus-vm --name nautilus-disk --resource-group $resource_group```