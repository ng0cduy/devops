```bash
#!/bin/bash
set -eoux pipefail
ec2_name=$1

# 1. Get the Instance ID of the instance named 'datacenter-ec2'
instance_id=$(aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=$ec2_name" \
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

echo "Instance ID: $instance_id"

# 2. Terminate the instance
aws ec2 terminate-instances \
    --instance-ids $instance_id \
    --region us-east-1

# 3. Wait for the instance to be fully terminated
echo "Waiting for instance to terminate..."
aws ec2 wait instance-terminated \
    --instance-ids $instance_id \
    --region us-east-1
```