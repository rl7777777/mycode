#!/usr/bin/python
#edit by jackren
import psutil
import json
import sys


def get_list():
    list = []
    zabbix_json = {}
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.exe().split('/')[-1] == 'node' and 'data' in p.name():
            dd_name = p.cwd().split('/')[-1]
            dic = {}
            dic['{#DDMS_NAME}'] = dd_name
            list.append(dic)
    zabbix_json['data'] = list
    data = json.dumps(zabbix_json,indent = 4,sort_keys = True,separators = (',',':'))
    print data


def get_mem(name):
    for pid in psutil.pids():
        p = psutil.Process(pid)    
        if p.exe().split('/')[-1] == 'node' and 'data' in p.name():    
            if p.cwd().split('/')[-1] == name:
                mem = p.memory_info()[0]
                print mem

def get_cpu(name):
    for pid in psutil.pids():
        p = psutil.Process(pid)    
        if p.exe().split('/')[-1] == 'node' and 'data' in p.name():    
            if p.cwd().split('/')[-1] == name:
                cpu_p = p.cpu_percent()
                print cpu_p


if len(sys.argv) == 1: 
    try:
        get_list()
    except Exception,e:
        print 'something wrong\n',e  

elif sys.argv[1] == 'mem':
    try:
        get_mem(sys.argv[2])
    except Exception,e:
        print 'something wrong\n',e


elif sys.argv[1] == 'cpu':
    try:
        get_cpu(sys.argv[2])
    except Exception,e:
        print 'something wrong\n',e        

else:
    print "Usage:ERROR"
