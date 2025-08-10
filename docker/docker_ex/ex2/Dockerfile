# Exercise 2: Serve a Static HTML Page

FROM redhat/ubi9:latest

# Install Nginx
RUN dnf install -y nginx && \
    dnf clean all

COPY index.html /usr/share/nginx/html/index.html

# Expose port 8080
EXPOSE 9090