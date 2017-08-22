#!/usr/bin/python3
"""
    Fabric script that creates and distributes an archive
    on my web servers, using deploy function
"""
from fabric.api import *
from fabric.operations import run, put, sudo, local
from datetime import datetime
import os
from importlib import import_module
pack_web = import_module('1-pack_web_static')
deploy_web = import_module('2-do_deploy_web_static')
env.hosts = ['66.70.184.249', '54.210.138.75']


def deploy():
    """
        deploy function that creates/distributes an archive
    """
    created_path = pack_web.do_pack()
    if created_path is None:
        return False
    return deploy_web.do_deploy(created_path)
