```resource_group=$(az group list | jq -r .[0].id | rev | cut -d"/" -f 1 | rev)```

```az network public-ip create --name devops-pip```