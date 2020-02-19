from flask import Flask, jsonify
import os
import sys

app = Flask (__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World'

@app.route('/configs')
def host_name():
    return jsonify(host_name)

@app.route('/configs/<hostname>')
def ip_add(hostname):
    return jsonify(device[hostname])
if __name__ == '__main__':
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
    app.run(debug=True)




