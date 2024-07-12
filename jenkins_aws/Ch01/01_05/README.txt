Jenkins and NGINX need to already be installed on your EC2 instance.
Connect to the instance via SSH and run the following commands:

    sudo su -
    unlink /etc/nginx/sites-enabled/default
    vim /etc/nginx/conf.d/jenkins.conf

Inside the jenkins.conf file, add the following contents:

    upstream jenkins {
        server 127.0.0.1:8080;
    }

    server {
        listen 80 default_server;
        listen [::]:80  default_server;
        location / {
            proxy_pass http://jenkins;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }

Now check the configuration:

    nginx -t

If there are any errors, edit the configuration file to fix them and then test
the configuration again.

Once the configuration is testing without errors, reload the configuration:

    systemctl reload nginx

Now open a browser to the instance's address and look for the "Unlock Jenkins" page.
