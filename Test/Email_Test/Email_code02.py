import poplib
import email
import datetime
import time
from email.parser import Parser
from email.header import decode_header
import traceback
import sys
import telnetlib

def get_att(msg, str_day):
    print(123123123123123123123123)

def loginEmail(user, passWord):
    pop3_server = 'pop.126.com'
    str_day = str(datetime.date.today()).replace('-', '')
    print(str_day)
    
    try:
        telnetlib.Telnet(pop3_server, 995)
        server = poplib.POP3_SSL(pop3_server, 995, timeout=10)
    except:
        time.sleep(5)
        server = poplib.POP3(pop3_server, 110, timeout=10)
    
    print(server.getwelcome().decode('utf-8'))
    
    resp, mails, octets = server.list()
    print('resp------------------->>[%s]' %resp)
    print('mails------------------->>[%s]' %mails)
    print('octets------------------->>[%s]' %octets)
    index = len(mails)
    
    
    for i in range(1, index+1):
        resp, lines, octets = server.retr(i)
        print('for resp----------------->>>>>>[%s]' % resp)
        print('for lines----------------->>>>>>[%s]' % lines)
        print('for octets----------------->>>>>>[%s]' % octets)
        
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        print('msg_content-------------->>[%s]' % msg_content)
        msg.Parser().parsestr(msg_content)
        
        date1 = time.strptime(msg.get('Date')[0:24], '%a, %d %b %Y %H:%M:%S')
        date2 = time.strftime("%Y%m%d", date1)
        print('date1[%s]--------------------date2[%s]' % (date1, date2))
        if date2 < str_day:
            continue
        else:
            get_att(msg, str_day)
        
    server.quit()    

if __name__ == '__main__':
    user = input('邮箱：')
    password = input('校验码：')
    loginEmail(user, password)