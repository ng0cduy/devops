#!/bin/bash
set -e

if [ -z "$S3_BUCKET" ]; then
    echo "Error: S3_BUCKET environment variable is not set."
    exit 1
fi

echo "Starting S3 sync from s3://${S3_BUCKET}..."
mkdir -p /data/raw

aws s3 sync "s3://${S3_BUCKET}" /data/raw

echo "Compressing data..."

tar -czf /usr/share/nginx/html/backup.tar.gz -C /data/raw .

echo "Creating index.html..."
echo "<html>
<head><title>S3 Backup Service</title></head>
<body>
    <h1>S3 Data Backup</h1>
    <p>Data synced from s3://${S3_BUCKET}</p>
    <p><a href='backup.tar.gz'>Download backup.tar.gz</a></p>
    <p>Generated at: $(date)</p>
</body>
</html>" > /usr/share/nginx/html/index.html

echo "Cleanup temporary data..."
rm -rf /data/raw

echo "Starting Nginx..."
exec nginx -g 'daemon off;'
