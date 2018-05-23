import pexpect
from getpass import getpass


def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()

    scon = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    scon.timeout = 7
    scon.expect('ssword:')

    scon.sendline(password)
    scon.expect('#')
    print scon.before

    scon.sendline('sh ip int bri')
    scon.expect('#')
    print scon.before

if __name__ == "__main__":
	main()
