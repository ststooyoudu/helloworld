import os
import sys
"""linux下需要加入这两行，因为本机和pycharm环境不一样，不加加载不到其他py文件"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
import json
from typing import Dict
from python_create_package import config as cf
import requests
import uuid

def get4AToken():
    paasDict: Dict[str, str] = {}
    paasDict['grant_type'] = cf.grant_type
    paasDict['client_id'] = cf.client_id
    paasDict['client_secret'] = cf.client_secret
    paasDict['scope'] = cf.scope
    url = cf.authURL + cf.tokenApplyURL + "?grant_type=" + paasDict['grant_type'] + "&client_id=" + paasDict[
        'client_id'] + "&client_secret=" + paasDict['client_secret'] + "&scope=" + paasDict['scope']
    print("url:" + url)
    response = requests.post(url, paasDict)  # 调取token的api
    content = response.content
    tokenContent = json.loads(content.decode('utf-8'))
    token = tokenContent['access_token']
    print(content)
    return token

def getForPasswordToken():
    payload = json.dumps({"params": {"account": "zhangyu","password": "Paas1234@", "tenantCode":"eab758e54994"}})
    headers = {'Content-Type': 'application/json'}
    url = cf.baseURL+cf.tokenURL
    print("url:"+url)
    response = requests.post(url,data=payload,headers=headers)
    content = response.content
    tokenContent = json.loads(content.decode('utf-8'))
    token = tokenContent['content']
    return token

def saveToken():
    token = getForPasswordToken()
    with open ('./Token.yaml','w') as f:
        f.write(token)
    f.close()
def getToken():
    with open('./Token.yaml','r') as f:
        token = f.readline()
    f.close()
    return token

def makeRequestSeq():
    """获取请求seq"""
    return str(uuid.uuid1()).replace("-", "")

def getHeaders():
    headers = {}
    if not getToken():
        saveToken()
    else:
        token = getToken()
    headers['Content-Type'] = 'application/json;charset=UTF-8'
    headers['Accept'] = 'application/json;charset=UTF-8'
#    headers['Content-Length'] = '135'  #加了之后CheckPackege.py会无响应
    headers['Authorization'] = "Bearer " + token
    headers['RequestSeq'] = makeRequestSeq()
    return headers

#saveToken()
#print(getToken())
#print(getHeaders())
#print(getForPasswordToken())
"""if __name__ == '__main__':
    token = getForPasswordToken()
    print(token)
    headers = getHeaders()
    print(headers)"""

