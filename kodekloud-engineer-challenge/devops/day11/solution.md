```bash
ssh banner@stapp03
```

```bash
# install tomcat
sudo yum install tomcat -y
```

```bash
sudo systemctl enable tomcat
sudo systemctl start tomcat
sudo systemctl status tomcat
```

```bash
#config the connector to use port 3000
sudo vi /etc/tomcat/server.xml
```

```bash
# restart tomcat
sudo systemctl restart tomcat
```

```bash
# copy .war file from jump host to app server 3
scp /tmp/ROOT.war banner@stapp03:/tmp
```

```bash
# Move to tomcat webapps folder
sudo mv /tmp/ROOT.war /var/lib/tomcat/webapps/
```

```bash
# test deployment
curl http://stapp01:3000
```