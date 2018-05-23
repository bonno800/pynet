import argparse
import time
from pprint import pprint
import pyeapi

def rm_vlan_func(remove):
   if args.name in current_vlans:
      print 'VLAN', args.name, 'exists.  Deleting now!'
      pynet_sw3.config(rm_vlan)
   else:
      print "VLAN", args.name, "does not exist"

def add_vlan_func(name):
   if args.name in current_vlans:
      print 'VLAN', args.name, 'already exists'
   else:
      print "VLAN", args.name, "does not exist"
      print "Now adding VLAN", args.name
      pynet_sw3.config(add_vlan)


def main():
   pprint(vlans)
   add_vlan_func(args.name)
   pprint(vlans)
   time.sleep(3)
   rm_vlan_func(args.NAME)
   pprint(vlans)




if __name__=='__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("--remove", help="VLAN Number")
   parser.add_argument("--name", help="VLAN name")
   args = parser.parse_args()
   pynet_sw3 = pyeapi.connect_to("pynet-sw3")
   vlans_retreive = pynet_sw3.enable("show vlan")
   vlans_list_strip = vlans_retreive[0]
   #pprint(vlans_list_strip)
   vlans_dict = vlans_list_strip['result']
   vlans = vlans_dict['vlans']
   current_vlans = vlans.keys()
   rm_vlan = ['no', args.remove]
   add_vlan = [args.name]
   pprint(current_vlans)
   main()


