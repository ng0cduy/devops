```bash
#!/bin/bash
set -eoux pipefail
volume_name=$1
snapshot_name=$2
vol_id=$(aws ec2 describe-volumes \
    --filters Name=tag:Name,Values=$volume_name \
    --region us-east-1 \
    --query "Volumes[0].VolumeId" \
    --output text)

echo "Volume ID: $vol_id"

# 2. Create the snapshot with description and Name tag
snap_id=$(aws ec2 create-snapshot \
    --volume-id $vol_id \
    --description "nautilus Snapshot" \
    --tag-specifications "ResourceType=snapshot,Tags=[{Key=Name,Value=$snapshot_name}]" \
    --region us-east-1 \
    --query "SnapshotId" \
    --output text)

echo "Snapshot ID: $snap_id"

# 3. Wait for the snapshot to be completed
echo "Waiting for snapshot to complete..."
aws ec2 wait snapshot-completed --snapshot-ids

```