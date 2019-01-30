#!/usr/bin/python

import psutil
import json
import sys
import subprocess
import time

def get_list():
    list = []
    zabbix_json = {}
    for proc in psutil.process_iter():
        p = proc.as_dict(attrs=['name','cwd','exe'])
        if p['exe'].split('/')[-1] == 'node' :
            dd_name = p['cwd'].split('/')[-1]
            dic = {}
            dic['{#DDMS_NAME}'] = dd_name
            list.append(dic)
    zabbix_json['data'] = list
    data = json.dumps(zabbix_json,indent = 4,sort_keys = True,separators = (',',':'))
    print data


def get_mem(name):
    for proc in psutil.process_iter():
        p = proc.as_dict(attrs=['name','cwd','exe','pid','memory_info'])
        if p['exe'].split('/')[-1] == 'node' :
            if p['cwd'].split('/')[-1] == name:
                mem = p['memory_info'][0]
                print mem


def get_cpu(name):
    for proc in psutil.process_iter():
        p = proc.as_dict(attrs=['name','cwd','exe','pid','cpu_percent'])
        if p['exe'].split('/')[-1] == 'node' :
            if p['cwd'].split('/')[-1] == name:
                cpu = proc.cpu_percent(interval=1)
                print cpu



if  __name__ == '__main__':
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
