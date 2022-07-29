
from selenium import webdriver
import random
import json
from time import sleep
from selenium.webdriver.common.by import By



def clickIn(username,passwd):
    # Chrome
    driver = webdriver.Chrome()
    # 104打卡網址
    driver.get("https://pro.104.com.tw/psc2")
    # 切換到頁面
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(4)
    # 清除輸入框內容、輸入帳號密碼，這邊用json取代
    loginUserName = driver.find_element(By.XPATH,"//*[@data-qa-id='loginUserName']")
    loginPassword = driver.find_element(By.XPATH,"//*[@data-qa-id='loginPassword']")
    submitButtom = driver.find_element(By.XPATH,"//*[@data-qa-id='loginButton']")   
    

    loginUserName.clear()
    loginPassword.clear()   

    loginUserName.send_keys(username)
    loginPassword.send_keys(passwd)
    submitButtom.click()    
    
    

    # 打開所有頁面
    windows = driver.window_handles
    # 切換到最新的頁面
    driver.switch_to.window(windows[0])
    # 隨機延後時間
    sleep(random.randint(5, 10))    

    clockButtom = driver.find_element(By.XPATH,"//*[@class='btn btn-white btn-lg btn-block']")
    clockButtom.click()
    sleep(1)
    # 關閉視窗
    driver.close()
    return 'done'

with open('member.json') as f:
    setting = json.load(f)
    members = setting['account']
   
for i in range(len(members)):
    clickIn(members[i]['userName'],members[i]['passWord'])
