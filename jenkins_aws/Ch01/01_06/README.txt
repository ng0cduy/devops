To retrieve the inital admin password, connect to the server where Jenkins is
running and execute the following commands:

    sudo su -
    cat /var/lib/jenkins/secrets/initialAdminPassword

Copy the output from the `cat` command and paste it into the Jenkins browser window prompting for the initial admin password.

