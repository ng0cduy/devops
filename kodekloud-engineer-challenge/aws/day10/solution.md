```
allocaltionID=$(aws ec2 describe-addresses --filters "Name=tag:Name,Values=xfusion-ec2-eip" --region us-east-1 --query "Addresses[0].AllocationId" --output text)
```

```
ec2ID=$(aws ec2 describe-instances     --filters "Name=tag:Name,Values=devops-ec2"     --query "Reservations[*].Instances[*].InstanceId"     --output text)
```


```
aws ec2 associate-address --instance-id $ec2ID --allocation-id $allocaltionID --region us-east-1
```