from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet1 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username' : 'pyclass',
	'password': password,
}

pynet2 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username' : 'pyclass',
	'password': password,
	'port' : 8022,
}

juniper_srx = {
	'device_type': 'juniper',
	'ip': '50.76.53.27',
	'username' : 'pyclass',
	'password': password,
	'port' : 9822,
}


pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
pynet_srx = ConnectHandler(**juniper_srx)

output1 = pynet_rtr1.send_command("show arp")
output2 = pynet_rtr2.send_command("show arp")
output3 = pynet_srx.send_command("show arp")

print output1
print output2
print output3
