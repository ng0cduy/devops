```resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)```

```az vm create --name datacenter-vm --image Ubuntu2204 --size Standard_B2s --admin-username azureuser --generate-ssh-keys --storage-sku Standard_LRS --os-disk-size-gb 30  --resource-group $resource-group```