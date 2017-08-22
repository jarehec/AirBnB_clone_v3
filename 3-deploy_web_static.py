#!/usr/bin/python3
"""
    Fabric script that creates and distributes an archive
    on my web servers, using deploy function
"""
from fabric.api import *
from fabric.operations import run, put, sudo, local
from datetime import datetime
env.hosts = ['66.70.184.249', '54.210.138.75']

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
        return archive


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    try:
        archive = archive_path.split("/")
        archive = archive[1]
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("mkdir -p /data/web_static/releases/{}/".format(folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(new_archive, folder[0]))
        run("mv /data/web_static/releases/{}/web_static/*"
            " /data/web_static/releases/{}"
            .format(folder[0], folder[0]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder[0]))
        run("rm /tmp/{}".format(archive))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current"
            .format(folder[0]))
        return True
    except:
        return False


def deploy():
    """
        deploy function that creates/distributes an archive
    """
    created_path = do_pack()
    if created_path is None:
        return False
    return do_deploy(created_path)
