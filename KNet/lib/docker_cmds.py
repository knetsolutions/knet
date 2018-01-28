'''Copyright 2018 KNet Solutions, India, http://knetsolutions.in

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import sys
import KNet.lib.utils as utils
import os
from KNet.lib.logger import logger as log

def create_container(name, img):
    # sudo docker run -itd --name=node1  ubuntu:trusty
    n = "--name=" + name
    cmd = ['sudo', 'docker', 'run', '-itd', n, img]
    return utils.run_cmd(cmd)


def stop_container(name):
    # sudo docker stop node1
    cmd = ['sudo', 'docker', 'stop', name]
    return utils.run_cmd(cmd)


def delete_container(name):
    cmd = ['sudo', 'docker', 'rm', name]
    return utils.run_cmd(cmd)


def run_ping_in_container(name, ip):
    # sudo docker exec -it a3 ping 10.20.20.2 -c 5
    cmd = ['sudo', 'docker', 'exec', '-t', name, 'ping', '-A', '-c', '5', ip]
    return utils.run_cmd(cmd)


def run_iperfs_in_container(name):
    # sudo docker exec -it a3 iperf -s &
    # note: background process doesnt work in utils.run_cmd
    cmd = "sudo docker exec -t " + name + "  iperf -s &"
    log.debug(cmd)
    return os.system(cmd)

def run_iperf_udps_in_container(name):
    # sudo docker exec -it a3 iperf -s &
    # note: background process doesnt work in utils.run_cmd
    cmd = "sudo docker exec -t " + name + "  iperf -u -s &"
    log.debug(cmd)
    return os.system(cmd)

def run_iperf_udpc_in_container(name, serverip, bandwidth, connections):
    # sudo docker exec -it a3 iperf -c 10.10.10.1 -P 5
    bandwidth = str(bandwidth) + "m"
    cmd = ['sudo', 'docker', 'exec', '-t', name, 'iperf', '-u', '-c',
           serverip, '-b', bandwidth, '-P', connections]
    return utils.run_cmd(cmd)


def run_iperfc_in_container(name, serverip, connections=1):
    # sudo docker exec -it a3 iperf -c 10.10.10.1 -P 5
    cmd = ['sudo', 'docker', 'exec', '-t', name, 'iperf', '-c',
           serverip, '-P', connections]
    return utils.run_cmd(cmd)


def run_pkill_in_container(name, pname):
    # sudo docker exec -it a3 pkill -9 iperf
    cmd = ['sudo', 'docker', 'exec', '-t', name, 'pkill', '-9', pname]
    return utils.run_cmd(cmd)


# Not used
def verify_image_exits(img):
    img_name, img_version = img.split(':')
    # sudo docker images ubuntu:trusty
    cmd = ['sudo', 'docker', 'images', img]
    response = utils.run_cmd(cmd)
    # verify the img exists  in the output
    if img_name in response and img_version in response:
        return {"result": "pass", "detail": response}
    else:
        return {"result": "fail", "detail": response}
