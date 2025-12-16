```bash
#!/bin/bash
ec2_name=$1
volume_name=$2
device=$3
ec2ID=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=$ec2_name" --query "Reservations[*].Instances[*].InstanceId" --output text)

volume_id=$(aws ec2 describe-volumes --filters "Name=tag:Name,Values=$volume_name" --region us-east-1 --query "Volumes[*].VolumeId" --output text)

# Attach the volume
aws ec2 attach-volume --volume-id $volume_id --instance-id $ec2ID --device $device

```