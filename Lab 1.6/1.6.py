import os
import re

path = "C:\D\seafile\Seafile\p4ne_training\config_files"
dirs = os.listdir( path )
ip_add = []

for conf in dirs:
#    print (conf)
    with open("C:\D\seafile\Seafile\p4ne_training\config_files\%s" %conf) as f:
        for line in f:
            print (line)
            t = re.match('ip address(. *)', line)
            print (t)
            ip_add.append(t)

for n in (sorted(set(ip_add))):
    print(n)
