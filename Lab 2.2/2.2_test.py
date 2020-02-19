import os
import sys

device = {}
host_name = []
ip_add = set()
path = "C:\D\seafile\Seafile\p4ne_training\config_files"
dirs = os.listdir(path)
for conf in dirs:
    with open("C:\D\seafile\Seafile\p4ne_training\config_files\%s" % conf) as f:
        for line in f:
            if "hostname" in line:
                curr_host_name = line.replace('hostname', '').strip()
                host_name.append(curr_host_name)
                device[curr_host_name] = []
#                print (curr_host_name)
                break
        for line in f:
            if "ip address" in line:
                if "255" in line:
                    ip_add = line.replace('ip address', '').strip()
#                    print (ip_add)
                    device[curr_host_name].append(ip_add)
print (device)