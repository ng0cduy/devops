FROM redhat/ubi9-minimal:latest

RUN microdnf install -y ncurses-base python3 python3-pip bash nginx curl-minimal unzip \
    && microdnf clean all

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

COPY sync_and_compress.sh /sync_and_compress.sh

RUN chmod +x /sync_and_compress.sh

ENTRYPOINT [ "/sync_and_compress.sh" ]