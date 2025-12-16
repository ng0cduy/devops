```bash
resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)
```

```bash
# Deallocate the VM
az vm deallocate --resource-group $resourceGroup --name $vm
```

```bash
# Resize the VM
az vm resize --resource-group $resourceGroup --name $vm --size $size
```

```bash
# Start the VM
az vm start --resource-group $resourceGroup --name $vm
```

```
reference:
https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm?tabs=cli
```