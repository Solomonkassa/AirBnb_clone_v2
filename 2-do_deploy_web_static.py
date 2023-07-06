#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['54.237.117.138', '100.26.216.97']  # Replace with your server IP addresses or hostnames
env.user = 'ubuntu'  # Replace with your username
env.key_filename = '~/.ssh/school'  # Replace with the path to your SSH private key


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]

        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the /data/web_static/releases/ directory
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_filename, archive_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the uncompressed folder to the parent folder
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version of your code
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed:", str(e))
        return False
