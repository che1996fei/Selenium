from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 隐式等待
browser = webdriver.Chrome()  # 声明浏览器并初始化
browser.implicitly_wait(10)  # 实现隐式等待10s
browser.get('http://www.zhihu.com/explore')  # 请求网页
input = browser.find_element_by_class_name('zu-top-add-question')  # 获取节点
print(input)  # 打印节点

# 显式等待
browser = webdriver.Chrome()  # 声明浏览器并初始化
browser.get('http://www.zhihu.com/explore')  # 请求网页
wait = WebDriverWait(browser, 10)  # 指定最长等待时间
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))  # 调用until(),传入等待条件
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#zh-top-search-form > button')))  # 调用until(),传入等待条件
print(input, button)

# 前进和后退
browser = webdriver.Chrome()  # 声明浏览器并初始化
browser.get('http://www.baidu.com/')
browser.get('https://www.zhihu.com/explore')
browser.get('https://www.sina.com.cn/')
browser.back()  # 后退
time.sleep(1)  # 延时1s
browser.forward()  # 前进


