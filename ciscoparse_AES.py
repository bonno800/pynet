from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")






cryptos = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

for crypto in cryptos:
      # if 'AES' in cryptos:
       #   continue
      # else:
         chill = crypto.children
         print crypto.text
         for child in chill:
           print child.text


