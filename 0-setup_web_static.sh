#!/usr/bin/env bash
#Setup Web Servers for deployment
if [ ! -x /usr/sbin/nginx ];
then
    apt-get update
    apt-get install nginx -y
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "Hello, Test!" | sudo tee /data/web_static/releases/test/index.html
ln -snf /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sed -i '72i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart
