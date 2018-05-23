from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT1 = 7961
SNMP_PORT2 = 8061

pynet_rtr1 = ('50.76.53.27', COMMUNITY_STRING, SNMP_PORT1)

pynet_rtr2 = ('50.76.53.27', COMMUNITY_STRING, SNMP_PORT2)

snmp_rtr1_MIB2sysNAME = snmp_get_oid(pynet_rtr1, oid='1.3.6.1.2.1.1.5.0', display_errors=True)

snmp_rtr2_MIB2sysNAME = snmp_get_oid(pynet_rtr2, oid='1.3.6.1.2.1.1.5.0', display_errors=True)

snmp_rtr1_MIB2sysDescr = snmp_get_oid(pynet_rtr1, oid='1.3.6.1.2.1.1.1.0', display_errors=True)
snmp_rtr2_MIB2sysDescr = snmp_get_oid(pynet_rtr2, oid='1.3.6.1.2.1.1.1.0', display_errors=True)

output1 = snmp_extract(snmp_rtr1_MIB2sysNAME)
output2 = snmp_extract(snmp_rtr2_MIB2sysNAME) 

output3 = snmp_extract(snmp_rtr1_MIB2sysDescr)
output4 = snmp_extract(snmp_rtr2_MIB2sysDescr) 

print output1

print output2

print output3

print output4
