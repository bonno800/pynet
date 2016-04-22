import telnetlib
import time

host = '50.76.53.27'
port = 23
timeout = 10

username = 'pyclass'
password = '88newclass'

session = telnetlib.Telnet(host, port, timeout)
print 'connecting...'
time.sleep(1)
session.read_until('name')
time.sleep(1)
print 'logging in'
session.write(username + '\n')
session.read_until('word')
time.sleep(1)
session.write(password + '\n')
time.sleep(1)
session.read_until('#')
time.sleep(1)
print 'executing command'
session.write('sh ip int bri\n')

sh_int = session.read_until('#')

print sh_int

session.close()



