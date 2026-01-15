FROM nginx:alpine

RUN apk add --no-cache \
    aws-cli \
    bash \
    tar

COPY script.sh /script.sh
RUN chmod +x /script.sh

ENV S3_BUCKET=example-bucket

# Expose port 80 for the web server
EXPOSE 80

# Set the entrypoint to the script
ENTRYPOINT ["/script.sh"]
