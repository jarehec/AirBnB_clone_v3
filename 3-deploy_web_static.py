#!/usr/bin/python3
"""
    Fabric script that creates and distributes an archive
    on my web servers, using deploy function
"""
from fabric.api import *
pack_web = __import__('1-pack_web_static')
deploy_web = __import__('2-do_deploy_web_static')


def deploy():
    """
        deploy function that creates/distributes an archive
    """
    created_path = pack_web.do_pack()
    if created_path is None:
        return False
    return(deploy_web.do_deploy(created_path))
