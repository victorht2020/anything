# Create base64 file

import os
import base64
import datetime
import time



def Create_file(path, name, data = None):
    ext = time.time()
    file_name = '{}/{}.{}'.format(path, name, ext)
    date = datetime.datetime.strftime(datetime.datetime.now(), 'Date: \t%d/%m/%Y %H:%M')
    maintainer = 'Maintainer: \t'+'Victor Tamashiro'
    email = 'Email: \t'+'victorht2020@git.com'
    basic = '''#
# {}
# {}
# {}
'''.format(date, maintainer, email)
    if data:
        basic = '{}\n{}\n'.format(basic, data)
    with open(file_name,'w+') as file:
        file.write(basic)

def Base64(entrada):
    entrada = entrada.encode('utf-8')
    #entrada = bytes(entrada, 'utf-8')
    return base64.b64encode(entrada)

def Lines():
    raw = ''
    while 1:
        new = input()
        if not new:
            break
        else:
            raw = raw+'\n'+new
    return raw

if __name__ == '__main__':
    path = os.getcwd()
    raw = Lines()
    print(Base64(raw).decode())
    Create_file(path, 'output', raw)
