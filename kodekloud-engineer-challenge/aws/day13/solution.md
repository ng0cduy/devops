```bash
#!/bin/bash
ec2_name=$1
ami_name=$2
device=$3
# 1. Get the Instance ID of the instance named 'datacenter-ec2'
instance_id=$(aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=$ec2_name" \
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

echo "Instance ID: $instance_id"

# 2. Create the AMI named 'datacenter-ec2-ami'
# --no-reboot is optional but speeds up creation if consistency isn't critical
ami_id=$(aws ec2 create-image \
    --instance-id $instance_id \
    --name $ami_name \
    --no-reboot \
    --query "ImageId" \
    --output text)

echo "AMI ID: $ami_id"

# 3. Wait for the AMI to reach the 'available' state
echo "Waiting for AMI to be available..."
aws ec2 wait image-available --image-ids $ami_id
```