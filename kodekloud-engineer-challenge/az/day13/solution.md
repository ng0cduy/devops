```bash
resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)
```

```bash
# Verify the VM is running
vm_name=nautilus-vm

user=azureuser

az vm get-instance-view \
  --name $vm_name \
  --resource-group $resource_group \
  --query "instanceView.statuses[?starts_with(code,'PowerState/')].displayStatus" \
  -o tsv
```

```bash
# get public ip
public_ip=$(az vm list-ip-addresses --name $vm_name --resource-group $resource_group -o table | awk '{print $2}' | tail -1)
```

```bash
pub_key=$(cat /root/.ssh/id_rsa.pub)
```
```
ssh -o StrictHostKeyChecking=no azureuser@$public_ip "sudo mkdir -p /root/.ssh && echo '$pub_key' | sudo tee -a /root/.ssh/authorized_keys && sudo chmod 700 /root/.ssh && sudo chmod 600 /root/.ssh/authorized_keys"
```