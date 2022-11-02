#!/usr/bin/python3
""" distributes an archive to web servers """
from os import path
from fabric.api import put, run, cd, env

env.hosts = ['3.239.2.1', '18.207.207.9']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """ returns True if all operations are successful
        or False if file path doesn't exist
    """
    if not path.exists(archive_path):
        return False

    archive_name = archive_path[9:]

    remote_dir = '/data/web_static/releases/' + archive_name[:-4]

    put(archive_path, '/tmp')

    run('sudo mkdir -p {}'.format(remote_dir))

    with cd(remote_dir):
        run('sudo tar -xzf {}'.format('/tmp/' + archive_name))

    run('sudo rm /tmp/{}'.format(archive_name))

    run('sudo mv {}/web_static/* {}'.format(remote_dir, remote_dir))

    run('sudo rm -rf {}/web_static'.format(remote_dir))

    run('sudo rm /data/web_static/current')

    run('sudo ln -s {} /data/web_static/current'.format(remote_dir))

    print("New version deployed!")

    return True

