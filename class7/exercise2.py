import time
from pprint import pprint
import pyeapi

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
 
def rm_vlan(add_vlan):
   if any(add_vlan[0] in s for s in add_vlan):
      print 'VLAN exists!  Deleting now!'
      
   elif not add_vlan[0] in v:
      print 'adding VLAN!'
      pynet_sw3.config(add_vlan)



def add_vlan(add_vlan):
   if any(add_vlan[0] in s for s in add_vlan):
      print 'Error: VLAN exists!'
   elif not add_vlan[0] in v:
      print 'adding VLAN!'
      pynet_sw3.config(add_vlan)

#for k, v in vlans_dict.iteritems():
 #  add_vlan(['vlan 963', 'name NICK_B'])








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

