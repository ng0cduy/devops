```bash
resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)
```

```bash
vm_id=$(az vm show --resource-group $resource_group --name $vm_name --query "id" --output tsv)
```

```bash
az tag create --resource-id $vm_id --tags Environment=dev
```