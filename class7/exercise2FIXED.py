import time
from pprint import pprint
import pyeapi

def rm_vlan_func():
   if '963' in current_vlans:
      print 'VLAN 963 exists.  Deleting now!'
      pynet_sw3.config(rm_vlan)
   else:
      print "VLAN 963 does not exist"

def add_vlan_func():
   if '963' in current_vlans:
      print 'VLAN 963 already exists'
   else:
      print "VLAN 963 does not exist"
      print "Now adding VLAN 963"
      pynet_sw3.config(add_vlan)


def main():
   pprint(vlans)
   add_vlan_func()
   pprint(vlans)
   time.sleep(3)
   rm_vlan_func()
   pprint(vlans)




if __name__=='__main__':
   pynet_sw3 = pyeapi.connect_to("pynet-sw3")
   vlans_retreive = pynet_sw3.enable("show vlan")
   vlans_list_strip = vlans_retreive[0]
   #pprint(vlans_list_strip)
   vlans_dict = vlans_list_strip['result']
   vlans = vlans_dict['vlans']
   current_vlans = vlans.keys()
   rm_vlan = ['no vlan 963']
   add_vlan = ['vlan 963', 'name NICK_B']
   pprint(current_vlans)
   main()



