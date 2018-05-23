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

output0 = pynet_rtr2.send_command("enable")
pynet_rtr2.config_mode()
output2 = pynet_rtr2.send_command("logging buffered 6000")
output3 = pynet_rtr2.send_command("do sh run | s logging buffered")

print output0
print output2
print output3
