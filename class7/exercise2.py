import time
from pprint import pprint
import pyeapi


if __name__=='__main__":
   pynet_sw3 = pyeapi.connect_to("pynet-sw3")
   vlans_retreive = pynet_sw3.enable("show vlan")
   vlans_list_strip = vlans_retreive[0]
   #pprint(vlans_list_strip)
   vlans_dict = vlans_list_strip['result']
   vlans = vlans_dict['vlans']

#pprint(vlans)


#for k, v in vlans_dict.iteritems(): 
 #  add_vlan = ['vlan 963', 'name NICK_B']
  # if 'vlans' in v:
   #   if not vlan_number in v:
    #     pynet_sw3.config(add_vlan)
 
def rm_vlan_func(rm_vlan):
   if any(rm_vlan[0] in s for s in v):
      print 'VLAN exists!  Deleting now!'
      pynet_sw3.config(rm_vlan)
   else:
      print 'Error: VLAN does not exist!'


def add_vlan_func(add_vlan):
   if any(add_vlan[0] in s for s in v):
      print 'Error: VLAN exists!'
   else:
      print 'adding VLAN!'
      pynet_sw3.config(add_vlan)

pprint(vlans)

for k, v in vlans.iteritems():
   add_vlan_func(['vlan 963', 'name NICK_B'])

pprint(vlans)

time.sleep(3)

for k, v in vlans.iteritems():
   rm_vlan_func(['no vlan 963'])

pprint(vlans)

#for k, v in vlans.iteritems(): 
 #  add_vlan = ['vlan 963', 'name NICK_B']
  # if any(add_vlan[0] in s for s in add_vlan):
   #   print 'Error: VLAN exists!'
   #elif not add_vlan[0] in v:
    #  print 'adding VLAN!'
     # pynet_sw3.config(add_vlan)

#add_vlan = ['vlan 963', 'name NICK_B']

#pynet_sw3.config(add_vlan)

#remove_vlan = ['no vlan 963']

#time.sleep(5)

#pynet_sw3.config(remove_vlan)

