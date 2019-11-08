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
        data = []
        name = []
        a = psutil.pids()
        for i in a:
            p = psutil.Process(i)
            if p.name() == 'java':
                if '-jar' in p.cmdline():      #java进程list数组中包含 -jar 执行
                    name.append(p.cmdline()[p.cmdline().index('-jar')+1])     #cmdline数组-jar下标值后一位     
        for i in name:
            data.append({'{#JAVA_NAME}': i})
        print json.dumps({'data': data}, indent=2)
    except Exception,e:
        print e


def get_mem(name):
    mem = subprocess.Popen("ps aux | grep %s| grep -v grep |grep -v python|grep -v JVM_OPTS| awk '{print $6}'" %name,shell=True,stdout = subprocess.PIPE)
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
