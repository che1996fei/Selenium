from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()  # 声明浏览器并初始化
browser.get('http://www.zhihu.com/explore')  # 请求网页
print(browser.page_source)  # 打印源代码

# 查找节点
input_first = browser.find_element_by_id('q')  # 根据ID获取输入框节点
input_second = browser.find_element_by_css_selector('#q')  # 根据CSS选择器获取输入框节点
input_third = browser.find_element_by_xpath('//*[@id="q"]')  # 根据XPath获取输入框节点
input_fourth = browser.find_element(By.ID, 'q')  # 用通用方法，需要传入两个参数：查找方式By和值
print(input_first, input_second, input_third, input_fourth)  # 分别打印出来

# 节点交互
input = browser.find_element_by_xpath('//*[@id="q"]')  # 根据XPath获取输入框节点
input.send_keys('奔驰')  # 输入文字
time.sleep(1)  # 延时1s
input.clear()  # 清空文字
input.send_keys('西安奔驰')  # 输入文字
button = browser.find_element(By.CSS_SELECTOR, '#zh-top-search-form > button') # 用通用方法，传入CSS选择器，获取搜索按钮
button.click()  #完成搜索动作
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 执行JavaScript

# 获取节点信息
logo = browser.find_element_by_id('zh-top-link-logo')  # 选择节点
print(logo.get_attribute('class'))  # 打印节点的属性
input = browser.find_element_by_class_name('zu-top-add-question')  # 选择节点
print(input.text)  # 打印节点的文本
print(input.id)  # 打印节点的ID
print(input.location)  # 打印节点的位置
print(input.tag_name)  # 打印节点的标签名称
print(input.size)  # 打印节点的大小


