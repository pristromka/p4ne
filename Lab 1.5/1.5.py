import os

path = "C:\D\seafile\Seafile\p4ne_training\config_files"
dirs = os.listdir( path )
ip_add = []

for conf in dirs:
#    print (conf)
    with open("C:\D\seafile\Seafile\p4ne_training\config_files\%s" %conf) as f:
        for line in f:
            if "ip address" in line:
                if "255" in line:
                    ip_add.append(line.replace('ip address', '').strip())

for n in (sorted(set(ip_add))):
    print(n)

