#!/usr/bin/env python3
#
# Copyright 2019 James Pace
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os
import sys
import subprocess

def run(in_args):
    parser = argparse.ArgumentParser(prog=sys.argv[0]+" run", description="Run a provided container using podman.")
    parser.add_argument("--container", "-c", help="Name of container to launch.")
    parser.add_argument("--volume", "-v", help="Volume on local machine to mount at same location in container.")
    parser.add_argument("--user", "-u", help="Username to login into container as.")
    args = parser.parse_args(in_args)

    username =  args.user
    if not args.user:
        username = os.environ["USER"]

    container = args.container
    if not args.container:
        container = "jwp-build-latest"
        
    volume = args.volume
    if not args.volume:
        volume = "/home/{}/Develop".format(username)

    # Include volume for ssh keys if it exists.
    ssh_text = ''
    if os.path.exists('/home/{}/.ssh'.format(username)):
        ssh_text = '--volume /home/{}/.ssh:/home/{}/.ssh:Z'.format(username, username)

    command = ('podman run --rm'
               ' --workdir /home/{username}'
               ' --user {username}'
               ' --userns=keep-id'
               ' --volume {volume}:{volume}:Z'
               ' {ssh_text}'
               ' -it {container} bash').format(
                       username=username,
                       container=container,
                       volume=volume,
                       ssh_text=ssh_text)
    print('Running: {}'.format(command))
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run(sys.argv[1:])
    