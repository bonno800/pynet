from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")




crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")


cryptos = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="set peer")

print cryptos

for crypto in cryptos:
  # crypto = cryptos[0]
    chill = crypto.all_children
    print crypto.text
    for child in chill:
      print child.text


