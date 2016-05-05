from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet2 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username' : 'pyclass',
	'password': password,
	'port' : 8022,
}

pynet_rtr2 = ConnectHandler(**pynet2)
pynet_rtr2.config_mode()

pynet_rtr2.send_config_from_file('config_file.txt')
output = pynet_rtr2.send_config_from_file('config_file.txt')
output2 = pynet_rtr2.send_command("sh run | inc logging")

print output
print output2

