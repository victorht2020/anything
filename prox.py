import requests
import random
#import requests[socks]

ip = 'http://icanhazip.com/'
#session = requests.session()
port = str(random.randint(10000,10100))
proxies = {'http':'socks4://127.0.0.1:'+port}
print(proxies)
r = requests.get(ip, proxies=proxies)
#r = session.get(ip)
print(r.text)
