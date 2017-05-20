#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import base64
import urllib
import urllib2
import mmap

def check(value):
    #mTable = open("C:\\Users\\Genius\\Desktop\\md5_hash_table.txt", 'r')
    #hTable = open("C:\\Users\\Genius\\Desktop\\sha1_hash_table.txt", 'r')

    if len(value) == 32:
            #found = mTable.read().find(value)
            with open("md5_hash_table.txt") as f:
                for line in f:
                    if value in line:
                        found = line[33:]
                        print "[+] md5 collision!! [FOUND]\n"
            
            return found
            #print "md5 collision!! [FOUND]"
            
    elif len(value) == 40:
            with open("sha1_hash_table.txt", 'r') as f:
                  for line in f:
                    if value in line:
                        found = line[41:]
                        print "[+] sha-1 collision!! [FOUND]\n"

            return found
     
            #found = hTable.read().find(value)
            #found=str(found)
            #print found[40:]
            #print "sha1 collision!! [FOUND]"
            #return found
    
url = "http://45.32.53.225/CTF/hash_crack/"
chk_url = "http://45.32.53.225/CTF/hash_crack/check.php?hash="

req = urllib2.Request(url)
res = urllib2.urlopen(req)
cookie = res.headers.get('Set-Cookie')

soup = BeautifulSoup(res.read(), 'lxml')
article = check(soup.findAll('pre')[0].string)  # pre 추출

chk_req = urllib2.Request(chk_url + str(article))
chk_req.add_header("Cookie",cookie)
chk_res = urllib2.urlopen(chk_req)

req.add_header("Cookie",cookie)

for i in range(48):
    # /decode_Me/ 29번줄 Cookie 추가해서 호출 
    res = urllib2.urlopen(req)
    read = res.read()

    soup = BeautifulSoup(read, 'lxml')
    article = check(soup.findAll('pre')[0].string)  # pre 추출
    
    print read

    chk_req = urllib2.Request(chk_url + str(article))
    chk_req.add_header("Cookie", cookie)
    chk_res = urllib2.urlopen(chk_req)
    print chk_res.read()

res = urllib2.urlopen(req)
print res.read()