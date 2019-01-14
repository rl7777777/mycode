#!/usr/bin/python
#edit by jackren
# python>2.7  root
import psutil
import json
import sys


def get_list():
    list = []
    zabbix_json = {}
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.exe().split('/')[-1] == 'node' and 'data' in p.name():  #获取进程路径包含node&data的进程名
            dd_name = p.cwd().split('/')[-1]      #获取nodejs进程名
            dic = {}
            dic['{#DDMS_NAME}'] = dd_name
            list.append(dic)
    zabbix_json['data'] = list
    data = json.dumps(zabbix_json,indent = 4,sort_keys = True,separators = (',',':'))   #按zabbix要求json格式标准输出
    print data


def get_mem(name):
    for pid in psutil.pids():
        p = psutil.Process(pid)    
        if p.exe().split('/')[-1] == 'node' and 'data' in p.name():    
            if p.cwd().split('/')[-1] == name:
                mem = p.memory_info()[0]
                print mem

def get_cpu(name):
    for proc in psutil.process_iter(attrs=['name','cwd','exe','pid']):
        p = proc.info
        if p['exe'].split('/')[-1] == 'node' and 'data' in p['name']:
            if p['cwd'].split('/')[-1] == name:
                cp = subprocess.Popen("ps aux | grep %s| grep -v grep | awk '{print $3}'" % (p['pid']) ,shell=True,stdout = subprocess.PIPE)
                out = cp.communicate()
                print out[0].strip('\n')


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


elif sys.argv[1] == 'cpu':
    try:
        get_cpu(sys.argv[2])
    except Exception,e:
        print 'something wrong\n',e        

else:
    print "Usage:ERROR"
#etc/zabbix_agentd.conf.d/zabbix_h5.conf:UserParameter=procMem[*], python /data/app/zabbix/agentscript/h5/ddms_discovery.py mem $1   2>&1
