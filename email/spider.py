#coding=utf-8

import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

yz_url = 'http://yz.kaoyan.com'

yz_html = requests.get(yz_url)
yz_html.encoding = 'utf-8'
yz_html = yz_html.text
# print yz_html.text

temp_file = open('temp_file.txt', 'w')
temp_file.write(yz_html)
temp_file.close()
print yz_url


# print 'spider'