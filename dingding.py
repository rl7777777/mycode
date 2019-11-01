#!/usr/bin/env python
#coding:utf-8
#zabbix  dingding monitor
import requests,json,sys,os,datetime
webhook="https://oapi.dingtalk.com/robot/send?access_token=c258a0baf24bcb"   
user=sys.argv[1]
text=sys.argv[3]
data={
     "msgtype": "markdown",
     "markdown": {
         "title": "zabbix monitor",
         "text": text
     },
    "at": {
        "atMobiles": [
            user
        ], 
        "isAtAll": True
    }
 }
headers = {'Content-Type': 'application/json'}
x=requests.post(url=webhook,data=json.dumps(data),headers=headers)
if os.path.exists("/usr/local/zabbix/log/dingding.log"):
    f=open("/usr/local/zabbix/log/dingding.log","a+")
else:
    f=open("/usr/local/zabbix/log/dingding.log","w+")
f.write("\n"+"--"*30)
if x.json()["errcode"] == 0:
    f.write("\n"+str(datetime.datetime.now())+"    "+str(user)+"    "+"发送成功"+"\n"+str(text))
    f.close()
else:
    f.write("\n"+str(datetime.datetime.now()) + "    " + str(user) + "    " + "发送失败" + "\n" + str(text))
    f.close()
    
