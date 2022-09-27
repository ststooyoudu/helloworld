import os
import sys
"""linux下需要加入这两行，因为本机和pycharm环境不一样，不加加载不到其他py文件"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from python_create_package import PaasApiUtils
from python_create_package import config
import requests
import datetime
import json


def get_payload(planCode, pipeLineCode):
    """payload里面需要填入的值是流水线名称和发布流水线名称"""
    payload = {"params": {}}
    payload["params"]["planCode"] = planCode
    payload["params"]["pipeLineCode"] = pipeLineCode
    payload["params"]["callbackUrl"] = "http://xxx.xx.xx.xx:xx/api/paas/CDExecutionDetail"
    payload["params"]["callbackType"] = "1"
    payload["params"]["flowId"] = datetime.datetime.now().strftime('%Y%m%d%H%M')
    payload["params"]["flowBuildId"] = datetime.datetime.now().strftime('%Y%m%d%H%M')
    payload["params"]["userName"] = config.username
    payload["params"]["passWord"] = config.password
    payload["params"]["releasePackage"] = config.sftpAddr
    return json.dumps(payload)


def requests_post(url, payload, headers): #发送post请求
    response = requests.post(url, data=payload, headers=headers)
#    print("url:" + url)
#    print(response)
    return response

def create_packge(planCode,pipeLineCode):  #创建流水线方法
    url = config.baseURL + config.cd_pipline
    headers = PaasApiUtils.getHeaders()
    payload = get_payload(planCode, pipeLineCode)
    """例如：get_payload('rhjc_wfw_20220921_temp', 'JC_C30_auto')"""
    print(payload)
    r = requests_post(url, payload, headers)
    if r.status_code == 401:
        PaasApiUtils.saveToken()
        print('Token过期，已重新获取！')
        headers = PaasApiUtils.getHeaders()
        r = requests_post(url, payload, headers)
    return r

def upload_packege():  #上次发布包方法
    pass

if __name__ == '__main__':
    
#    r = create_packge('rhjc_dt_202209241600', 'CS_C00')
    r = create_packge('rhjc_wfw_202209241600', 'JC_C30_auto')
    if r.status_code == 200:
        print("流水线创建成功")
    else:
        print("流水线创建失败")




