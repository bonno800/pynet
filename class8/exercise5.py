from datetime import datetime

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()
    
    start_time = datetime.now()


    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
        device_type = a_device.device_type
        port = a_device.port
        secret = ''
        ip = a_device.ip_address
        creds = a_device.credentials
        username = creds.username
        password = creds.password
        print device_type, port, ip, username, password
        remote_conn = ConnectHandler(device_type=device_type, ip=ip, username=username, password=password, port=port)
	print remote_conn.send_command_expect("show ver")

    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)       


if __name__ == "__main__":
    main()
