#!/usr/bin/python3
"""Generates from the contents of the web_static folder a .tgz archive."""
from fabric.api import local
import time


def do_pack():
    """Generate a .tgz archive from the content web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
