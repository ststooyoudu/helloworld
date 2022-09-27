import os
import sys
"""linux下需要加入这两行，因为本机和pycharm环境不一样，不加加载不到其他py文件"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from python_create_package import PaasApiUtils
from python_create_package import CreatePackge
from python_create_package import config
import requests
import datetime
import json

def get_payload(planCode):
    """传入流水线名称"""
    payload = {"params": {},"pageInfo": {}}
    payload["params"]["planCode"] = planCode
    payload["params"]["filterParam"] = {}
    payload["pageInfo"]["currentPage"] = 1
    payload["pageInfo"]["pageSize"] = 10
    payload["pageInfo"]["totalRecord"] = 2
    return json.dumps(payload)

def check_page_list(planCode):
    url = config.page_list
    list = []
    payload = get_payload(planCode)
    headers = PaasApiUtils.getHeaders()
    r = CreatePackge.requests_post(url, payload, headers)
    if r.status_code == 401:
        PaasApiUtils.saveToken()
        print('Token过期，已重新获取！')
        headers = PaasApiUtils.getHeaders()
        r = CreatePackge.requests_post(url, payload, headers)
    try:
        if r:
            content = json.loads(r.text)
            contentlist = content["content"]["list"][0]["releases"]
#            print(contentlist)
            num = len(contentlist)
            for i in range(num):
                list = []
                planReleaseId = contentlist[i]["planReleaseId"] #ep:20270
                releaseCode = contentlist[i]["releaseCode"]  #ep:WFWGRKH-RHIBOSS
                releaseName = contentlist[i]["releaseName"]  #ep:微服务_个人客户融合IBOSS_非配置中心
                list.append(planReleaseId)
                list.append(releaseCode)
                list.append(releaseName)
                planReleaseId = list[0]
                url = config.check_zip + "?" + "planReleaseId=" + str(planReleaseId)
                headers = PaasApiUtils.getHeaders()
                r = requests.get(url=url, headers=headers)
                if r.status_code == 401:
                    PaasApiUtils.saveToken()
                    print('Token过期，已重新获取！')
                    headers = PaasApiUtils.getHeaders()
                    r = CreatePackge.requests_post(url, headers)
                content = json.loads(r.text)
                zipName = content["content"]["packageName"]
                print("%-30s%-20s%-30s%-20s" % (myAlign(planCode.strip(), 50), myAlign(list[1], 50), myAlign(list[2], 50), myAlign(zipName, 50)))
#                if i > 1:
#                    print("%-30s%-20s%-30s%-20s" % (myAlign('-'), 50), myAlign(list[1], 50), myAlign(list[2], 50),myAlign(zipName, 50))
#                else:
#                    print("%-30s%-20s%-30s%-20s" % (myAlign(planCode.strip(), 50), myAlign(list[1], 50), myAlign(list[2], 50), myAlign(zipName, 50)))
    except:
        print("获取发布包信息失败！")


def check_packge(planCode):
    planReleaseId = check_page_list(planCode)[0]
    url = config.check_zip+"?"+"planReleaseId="+str(planReleaseId)
    headers = PaasApiUtils.getHeaders()
    r = requests.get(url=url, headers=headers)
    if r.status_code == 401:
        PaasApiUtils.saveToken()
        print('Token过期，已重新获取！')
        headers = PaasApiUtils.getHeaders()
        r = CreatePackge.requests_post(url,headers)
    content = json.loads(r.text)
    zipName = content["content"]["packageName"]    
    return zipName
#    print(zipName)
def myAlign(string, length=0):
    """网上找的应对中文对齐的函数"""
    if length == 0:
        return string
    slen = len(string)
    re = string
    if isinstance(string, str):
        placeholder = ' '
    else:
        placeholder = u'　'
    while slen < length:
        re += placeholder
        slen += 1
        return re


if __name__ == '__main__':
    with open('./list.ini','r') as f:
        listInfos = f.readlines()
        tplt = "{0:<30}{1:<20}{2:<25}{3:<30}"
        print(tplt.format("上线名称","发布名称","发布简介","发布包名称",chr(12288)))
        for planCode in listInfos:
            check_page_list(planCode)
