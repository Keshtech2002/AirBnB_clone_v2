#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from fabric.api import local
import time


def do_pack():
    """ returns .tgz archive if generated else None """

    local('mkdir -p versions')
    time_created = time.strftime("%Y%m%d%H%M%S")
    arch_path = 'versions/web_static_{}.tgz'.format(time_created)

    if local('tar -cvzf {} web_static'.format(arch_path)):
        return arch_path
    return None
