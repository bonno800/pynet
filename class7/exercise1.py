from pprint import pprint
import pyeapi

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

show_intf = pynet_sw3.enable("show interfaces")
show_intf = show_intf[0]['result']

# results = show_intf[1]
#results = show_intf['result']


show_intf = show_intf['interfaces']
#print show_intf
#pprint(show_intf)
oct_data = {}
for interface, int_values in show_intf.items():
   int_c = int_values.get('interfaceCounters', {})
   oct_data[interface] = (int_c.get('inOctets'), int_c.get('outOctets'))


print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")


for intf, octets in oct_data.items():
   print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])


