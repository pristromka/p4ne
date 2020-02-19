from pysnmp.hlapi import *

result == getCmd(SnmpEngine(),CommunityData("public", mpModel=0, UdpTransportTarget(("10.31.70.107", 161)),  ))