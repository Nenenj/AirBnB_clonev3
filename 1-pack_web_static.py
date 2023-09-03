#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo

"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None on failure.
    """
    try:
        # Create a directory named "versions" if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the archive name based on the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Use tar to create the archive
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        return None
