#!/usr/bin/python2.7
#-*- coding:utf-8 -*-
import requests
import json
import os
import sys

def sdd(txt):
    token = "2492026a43c522de916d44b09cea9ada0e61adf23ddcfb88eb634c1dd00dc3e6"
    rul = "https://oapi.dingtalk.com/robot/send?access_token=" + token
    #headers = {'Content-Type': 'application/json;charset=utf-8'}
    headers = {'Content-Type': 'application/json'}
    text1 = "{}".format(txt)
    #print(text1)
    Content=json.dumps({
       "msgtype": "text",
        "text": {
             "content": text1
        },
        "at": {
             "atMobiles": [
                 "18969099474"
            ],
            "isAtAll": "false"
        } 
    })

    try:
        print requests.post(url=rul,data=Content,headers=headers).content
        print(Content)
    except Exception as e:
        print("msg:",e)

def xx():
    msg = sys.argv[1]
    sdd(msg)
if __name__ == "__main__":
    xx()
