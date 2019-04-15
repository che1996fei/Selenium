from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import time

browser = webdriver.Chrome()  # 声明浏览器并初始化
wait = WebDriverWait(browser, 10)  # 指定最长等待时间

def search():
    try:
        browser.get('http://www.zhihu.com/explore')  # 请求网页
        input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q"]')))  # 根据XPath获取输入框节点
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zh-top-search-form > button'))) # 用通用方法，传入CSS选择器，获取搜索按钮
        input.send_keys('西安奔驰')  # 输入文字
        time.sleep(1)  # 延时1s
        button.click()  #完成搜索动作
    except TimeoutError:
        return search()

def get_prodcts():
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#SearchMain .ListShortcut .List .Card SearchResult-Card .List-item')))  # 用until(传入要等待的条件：节点加载出来，传入定位元组，用CSS选择器)
        html = browser.page_source  # 获得网页源代码
        doc = pq(html)  # 选择pyquery并初始化
        items = doc('#SearchMain .ListShortcut .List .Card SearchResult-Card .List-item').items()
        for item in items:
            product = {
                'title': item.find('.ContentItem-title').text(),
                'image': item.find('.RichText ztext CopyrightRichText-richText').text(),
            }
            print(product)
    except TimeoutError:
        return get_prodcts()


