import time
from pprint import pprint
import pyeapi

pynet_sw3 = pyeapi.connect_to("pynet-sw3")


vlans_retreive = pynet_sw3.enable("show vlan")


vlans_list_strip = vlans_retreive[0]


pprint(vlans_list_strip)

vlans_dict = vlans_list_strip['result']

#pprint(vlans)


for k, v in vlans_dict.iteritems():
   if 'vlans' in v:
      if not vlan_number in v:
         pynet_sw3.config(add_vlan) 

add_vlan = ['vlan 963', 'name NICK_B']

pynet_sw3.config(add_vlan)

remove_vlan = ['no vlan 963']

time.sleep(5)

pynet_sw3.config(remove_vlan)

