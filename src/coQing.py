import requests
import os
import time

fname = 'config.txt'
name = None
password = None
type = None
t=0

if  os.path.exists(fname):

    with open(fname, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        if len(lines) >= 1:
            name = (lines[0].replace(" ","")).replace("\n","")
        if len(lines) >= 2:
            password = (lines[1].replace(" ","")).replace("\n","")
        if len(lines)>=3:
            type = (lines[2].replace(" ","")).replace("\n","")
        if len(lines) >= 4:
            t = (lines[3].replace(" ", "")).replace("\n", "")

    if name == None or password == None or type == None or name == "" or password == "" or type == "":
        print("config.txt文件内容不正确")
        os.system('pause')
    else:
        print("正在等待电脑连上校园网的网线或者wifi")
        time.sleep(int(t))

        url = 'http://172.16.2.2/'
        data = {
            "callback": "dr1003",
            "DDDDD": name,
            "upass": password,
            "0MKKey": "123456",
            "R1": "0",
            "R2": "",
            "R3": type,
            "R6": "0",
            "para": "00",
            "v6ip": "",
            "terminal_type": "1",
            "lang": "zh-cn",
            "jsVersion": "4.1",
            "v": "6210",
            "lang": "zh"
        }
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "172.16.2.2",
            "Pragma": "no-cache",
            "Referer": "http://172.16.2.2/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        response = requests.post(url, data, headers=header).status_code
        # print("{}".format(response))

else:
    print("config.txt文件不存在")
    os.system('pause')
