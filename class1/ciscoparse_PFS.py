from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")






cryptos = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="pfs group2")

for crypto in cryptos:
       chill = crypto.all_children
       print crypto.text
       for child in chill:
          print child.text


