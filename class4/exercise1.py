import paramiko
from getpass import getpass
import time
import pprint


ip_addr = '50.76.53.27'
username = 'pyclass'
password = '88newclass'
port = 8022

remote_conn_pre=paramiko.SSHClient()
print remote_conn_pre

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_pre.invoke_shell()

output = remote_conn.recv(5000)
time.sleep(1)
print output
time.sleep(1)
output = remote_conn.send("term len 0\n")
time.sleep(1)
output = remote_conn.recv(5000)
time.sleep(1)
print output
output = remote_conn.send("show version\n")
time.sleep(1)
output = remote_conn.recv(99000)
time.sleep(1)
print output
