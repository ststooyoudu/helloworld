import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import requests
import urllib3
import pyautogui
import schedule


s =Service('C:\selenium\console-test\lib\chromedriver.exe')
driver = webdriver.Chrome(service=s)
account_items={'sunxing':'3edc#EDC','mengyuhao':'1qaz@WSX'}


def click_button(value): #点击函数
    click_name = driver.find_element(by=By.XPATH, value=value)
    ActionChains(driver).click(click_name).perform()
    time.sleep(2)
def send_text(value,text):   #输入函数
    send_name = driver.find_element(by=By.XPATH, value=value).send_keys(text)
#    ActionChains(driver).click(send_name).perform()
    time.sleep(2)
def check_in(user,passwd):
    ##########################进入主站
    if check_net() == 200:
        driver.get('http://xxhapp.js.cmcc:30002/jsjz-web/login')
        driver.maximize_window()
        time.sleep(4)
        send_text('/html/body/div[2]/form/div[1]/div/input',user)
        time.sleep(2)
        send_text('//*[@id="password"]',passwd)
        click_button('/html/body/div[2]/form/div[4]/button')
        click_button('//*[@id="workIn"]')
        time.sleep(2)
        click_button('/ html / body / div[1] / div[1] / div / div[4] / a / font') #退出登录下一个用户
        time.sleep(3)

#        driver.quit()
    else:
        disconnect_net()

def check_out(user,passwd):
    ##########################进入主站
    if check_net() == 200:
        driver.get('http://xxxxxx.com')
        driver.maximize_window()
        time.sleep(1)
        send_text('/html/body/div[2]/form/div[1]/div/input',user)
        send_text('//*[@id="password"]',passwd)
        click_button('/html/body/div[2]/form/div[4]/button') #登录
        current_handle = driver.current_window_handle #获取当前窗口
        click_button('//*[@id="attendanceDiv"]/div[1]/div[3]')  #日报
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle !=current_handle:
                driver.switch_to.window(handle)
                print(handle)
        time.sleep(2)
        now_handle = driver.current_window_handle
        print(current_handle)
        print(all_handles)
        print(now_handle)
        click_button('//*[@id="createWorkDailyItem2"]')  # 任务
        send_text('//*[@id="taskContent"]', '1、主干构建\n2、测试环境维护')
        click_button('/ html / body / div[3] / div[1] / button[1]')  #保存
        click_button('//*[@id="layui-layer1"]/div[3]/a')  #保存确定
#        click_button('/ html / body / div[3] / div[1] / button[2] / span') #提交
        driver.switch_to.window(current_handle) #切回主窗口
        click_button('//*[@id="workOut"]') #签入
        click_button('/ html / body / div[5] / div / div / div[2] / button[2]')  #确定
        time.sleep(2)
        click_button('/ html / body / div[1] / div[1] / div / div[4] / a / font')  # 退出登录下一个用户
        time.sleep(3)
    else:
        disconnect_net()


            
#######################################监控网络
def check_net():
    try :
        print("flag")
        requests.adapters.DEFAULT_RETRIES = 5
        requests.packages.urllib3.disable_warnings()  #忽视警告
        ss = requests.session()
        ss.keep_alive = False
        response = requests.get("http://xxxx.com",verify=False)
        if response.status_code == 200:
            print("网络正常！")
            return 200
        else:
            print("网络异常！正尝试恢复")
#            disconnect_net()
            return 400
    except:
        print('异常函数执行！')
        disconnect_net()

########################################网络重连
def disconnect_net():
    print('网络中断尝试恢复！......')
    os.startfile(r"C:\Program Files (x86)\SPES5.0\Composites\SPES\SPES5.exe")
    pyautogui.click(x=612, y=398)
    time.sleep(4)
    pyautogui.click(x=612, y=398)
    time.sleep(2)
    check_in()

############################################

def all_checkin():
    for user,passwd in account_items.items():
        print("当前用户："+user )
        check_in(user, passwd)

def all_checkout():
    for user,passwd in account_items.items():
        print("当前用户："+user )
        check_out(user, passwd)

############################设置定时任务
pyautogui.FAILSAFE = False
schedule.every().day.at("08:26").do(all_checkin)
schedule.every().day.at("18:11").do(all_checkout)
#all_checkin()
#all_checkout()
while True:
    print("进程运行中.....")
    schedule.run_pending()
    time.sleep(5)


