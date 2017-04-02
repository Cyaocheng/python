#!/usr/bin/python
#-*- coding: UTF-8 -*- 


import urllib2
import urllib
import re
import time
from random import choice


ip_list = ['112.124.43.16:8888', '211.102.219.131:80','58.176.21.13:8998','202.111.31.158:8080','113.109.26.56:808']

ip_item = choice(ip_list)
word_list = ["民生","科技","python教材","ubuntu程序", "suse版本"]
matchChinese = re.compile(u'(\"[\u4e00-\u9fa5]*\"\,)')


for item in word_list:
	key_word = urllib.quote(item)
	#print key_word

	url="https://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word="+key_word

	headers = {
		"GET":url,
		"Host":"sug.so.360.cn",
		"Referer":"https://www.so.com/",
		"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
	}

	enable_proxy = True 
	proxy_handler = urllib2.ProxyHandler({"http":'http://'+ip_item})
	null_proxy_handler = urllib2.ProxyHandler({})

	if enable_proxy:
		opener = urllib2.build_opener(proxy_handler)
	else: opener = urllib2.build_opener(null_proxy_handler)

	urllib2.install_opener(opener) 

	req = urllib2.Request(url)
	for key in headers:
		req.add_header(key,headers[key])

	html= urllib2.urlopen(req).read()

	#print html
	re_word = matchChinese.findall(html.decode("utf8"))
	for inter_item in re_word:
		print inter_item
	time.sleep(6)
