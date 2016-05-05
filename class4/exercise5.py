from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

NB_3850_8 = {
	'device_type': 'cisco_ios',
	'ip': '50.76.53.27',
	'username' : 'pyclass',
	'password': password,
	'port' : 8022,
}



nick_3850 = ConnectHandler(**NB_3850_8)

nick_3850.find_prompt()
nick_3850.exit_config_mode()
nick_3850.config_mode()
output = nick_3850.check_config_mode()

print 'In configuration mode:' ,  output
