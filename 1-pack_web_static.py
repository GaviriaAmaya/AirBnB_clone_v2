#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


def do_pack():
    """Paccking a file with fabric """
    local("sudo mkdir -p versions")
    dated = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_f = ("versions/web_static_{}.tgz").format(dated)
    local("sudo tar -cvzf {} web_static".format(file))
    return tar_f
