from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

import Queue
import threading
import time

def show_ver(q, a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, 
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    print
    print '#' * 80
    print remote_conn.send_command_expect("show ver")

q = Queue.Queue

def main():
    django.setup()
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for a_device in devices:
        my_thread = threading.Thread(target=show_ver, args=(q,a_device))
        my_thread.start()
        print threading.currentThread().getName(), 'Starting'
        time.sleep(1)
        print threading.currentThread().getName(), 'Exiting'

  #  main_thread = threading.currentThread()
   # for some_thread in threading.enumerate():
    #    if some_thread != main_thread:
     #       print some_thread

    print "\nElapsed time: " + str(datetime.now() - start_time)
    s = q.get()
    print s

if __name__ == "__main__":
    main()
