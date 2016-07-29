import time
from pprint import pprint
import pyeapi

def rm_vlan_func(rm_vlan):
   if k is 963 in vlans.keys():
      print 'VLAN exists!  Deleting now!'
      pynet_sw3.config(rm_vlan)
   else:
      print 'Error: VLAN does not exist!'


def add_vlan_func(add_vlan):
   if k is 963 in vlans.keys():
      print 'Error: VLAN exists!'
   else:
      print 'adding VLAN!'
      pynet_sw3.config(add_vlan)

def main():
   pprint(vlans)
   for k in vlans.keys():
      add_vlan_func(['vlan 963', 'name NICK_B'])
      pprint(vlans)
   time.sleep(3)
   for k in vlans.keys():
      rm_vlan_func(['no vlan 963'])
      pprint(vlans)




if __name__=='__main__':
   pynet_sw3 = pyeapi.connect_to("pynet-sw3")
   vlans_retreive = pynet_sw3.enable("show vlan")
   vlans_list_strip = vlans_retreive[0]
   #pprint(vlans_list_strip)
   vlans_dict = vlans_list_strip['result']
   vlans = vlans_dict['vlans']
   main()

