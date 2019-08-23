#!/usr/bin/env bash
#Setup Web Servers for deployment
if [ ! -x /usr/sbin/nginx ];
then
    sudo apt-get update
    sudo apt-get install nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
Header='<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'
sudo echo "$Header" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '72i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
