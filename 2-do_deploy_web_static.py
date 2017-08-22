#!/usr/bin/python3
"""
    Fabric script that distributes an archive to my web servers
"""
from fabric.api import *
env.hosts = ['137 web-01', '137 web-02']


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
