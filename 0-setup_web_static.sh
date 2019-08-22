#!/usr/bin/env bash
#Setup Web Servers for deployment
if [ ! -x /usr/sbin/nginx ];
then
    sudo apt-get update
    sudo apt-get install nginx
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo echo "HelloTest!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '72i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/defaultx
sudo service nginx restart
