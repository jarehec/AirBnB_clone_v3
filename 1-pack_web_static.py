#!/usr/bin/python3
"""
    Fabric script that generates tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    archive = ''
    archive += local("mkdir -p ./versions")
    archive += local("tar --create --verbose -z --file={} ./web_static"
                     .format(file_name))
    if archive is None:
        return None
    else:
        return file_name
