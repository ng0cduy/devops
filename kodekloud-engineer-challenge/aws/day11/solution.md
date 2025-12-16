```bash
#!/bin/bash
ec2_name=$1
eni_name=$2
index=$3
ec2ID=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=$ec2_name" --query "Reservations[*].Instances[*].InstanceId" --output text)

eni_id=$(aws ec2 describe-network-interfaces --region us-east-1 --filters "Name=tag:Name,Values=$eni_name" --query "NetworkInterfaces[].NetworkInterfaceId" --output text)

aws ec2 attach-network-interface --network-interface-id $eni_id --instance-id $ec2ID --device-index $index

# Check before submit
aws ec2 describe-network-interfaces \
    --region us-east-1 \
    --network-interface-id $eni_id \
    --query "NetworkInterfaces[].Attachment.Status" --output text
```