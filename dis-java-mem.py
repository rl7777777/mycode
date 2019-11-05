#!/usr/bin/python
# -*- coding: utf8 -*-
#edit by jackren
# python>2.7  root
import psutil
import json
import sys
import re
import subprocess
import os


def get_list():
    try:
        list = []
        name = []
        zabbix_json = {}
        a = psutil.pids()
        for i in a:
            p = psutil.Process(i)
            if p.name() == 'java':
               dd_name=p.cmdline()[-1].split('/')[-1]
               #print dd_name
               dic = {}
               dic['{#JAVA_NAME}'] = dd_name
               list.append(dic)
        zabbix_json['data'] = list
        data = json.dumps(zabbix_json,indent = 4,sort_keys = True,separators = (',',':')) 
        print data
    except Exception,e:
        print e


def get_mem(name):
    mem = subprocess.Popen("ps aux | grep %s| grep -v grep |grep -v python| awk '{print $6}'" %name,shell=True,stdout = subprocess.PIPE)
    #tmp = os.popen("ps aux|grep %s|grep -v grep|grep -v python|awk '{print$11}'" %name).readlines()
    out = mem.communicate()[0].strip('\n')
    print out
    #print '--------------'

if len(sys.argv) == 1:        #不加参数输出进程名
    try:
        get_list()
    except Exception,e:
        print 'something wrong\n',e  

elif sys.argv[1] == 'mem':
    try:
        get_mem(sys.argv[2])
    except Exception,e:
        print 'something wrong\n',e


else:
    print "Usage:ERROR"
    
#UserParameter=java.name, /etc/zabbix/scripts/disco.py 
#UserParameter=java.mem[*], /etc/zabbix/scripts/disco.py mem $1
