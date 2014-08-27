#!/usr/bin/python3

import urllib3
import datetime
import time


IPAddr = '<your router\'s adress>'
url_clog = 'http://' + IPAddr + '/index.cgi/syslog_common_c.log'
url_slog = 'http://' + IPAddr + '/index.cgi/syslog_security_c.log'
BasicAuth = 'Basic <base64(<username>:<password>)'
filepath = '<path you want save log to>'

def getlog(url):
    http = urllib3.PoolManager()
    header = {'Authorization' : BasicAuth}
    request = http.request('GET', url, headers=header)
    
    return request

def savelog(request,filename):

    if request.status == 200:
        f = open(filename, 'wb')
        f.write(request.data)
    else:
        f = open(filename, 'w+')
        str = 'Error: %d \nFailed to get log.' %request.status
        f.write(str)

    f.close()

def main():
    while True:
        filename = 'log_%s.txt'%datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
        
        savelog(getlog(url_clog),filepath+'common/'+''+'common_'+filename)
        savelog(getlog(url_slog),filepath+'security/'+'security_'filename)
        time.sleep(60*60*24)
        
if __name__ == '__main__':
    main()
