#!/usr/bin/env bash
#Setup Web Servers for deployment
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
HelloTest="<html>
<head>
</head>
<body>
holberton school
</body>
</html>"
sudo echo "$HelloTest" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/ && sudo chgrp -R ubuntu /data/
sed -i '37i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart
