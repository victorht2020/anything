# Test proxies
exit()
# Crash
import os
import requests
import time
import random
#import requests[socks]

ip = 'http://icanhazip.com/'
ports = []

def teste(port):
    proxies = {'http':'socks4://127.0.0.1:'+port}
    #print(proxies)
    pid = os.fork()
    if pid == 0:
        child(proxies)


def child(proxies):
    r = requests.get(ip, proxies=proxies)
    print((r.text).replace('\n',''))
    exit()

while 1:

    port = str(random.randint(10000,10100))
    while port in ports:
        port = str(random.randint(10000,10100))
    teste(port)
    ports.append(port)
    if len(ports) >= 50:
        del ports[0:5]
