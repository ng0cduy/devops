#!/bin/bash
set -eoux pipefail

LOCAL_DIR="$1"
S3_DIR="$2"

echo "Syncing from s3://$S3_DIR bucket to local directory $LOCAL_DIR"

mkdir -p "$LOCAL_DIR"
aws s3 sync "s3://$S3_DIR" "$LOCAL_DIR"


nginx_index_dir="/usr/share/nginx/html"

echo "Compress s3 data to $nginx_index_dir"
tar -czf "$nginx_index_dir/s3_data.tar.gz" -C "$LOCAL_DIR" .

echo "<html><body><h1>Operation Complete</h1><a href='s3_data.tar.gz'>Download Compressed Data</a></body></html>" > $nginx_index_dir/index.html
nginx -g "daemon off;"