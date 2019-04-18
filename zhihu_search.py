from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

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
        get_prodcts()
    except TimeoutError:
        return search()

def get_prodcts():
    for i in range(10):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        ActionChains(browser).key_down(Keys.DOWN).perform()
        time.sleep(5)
    try:
        html = browser.page_source  # 获得网页源代码
        tree = etree.HTML(html)
        items = tree.xpath('//*[@id="SearchMain"]/div/div/div/div//div')
        for item in items:
            title = item.xpath('./div/div/h2//a/span//text()')
            comment = item.xpath('./div/div[1]/span//text()')
            attitudes_count = item.xpath('./div/div/div[2]/span/button[1]//text()')
            if title == []:
                pass
            else:
                print(title)
            if comment == []:
                pass
            else:
                print(comment)
            if attitudes_count == []:
                pass
            else:
                if attitudes_count:
                    attitudes_count = attitudes_count[1]
                else:
                    attitudes_count = ""
                print(attitudes_count)
    except Exception as e:
        print(e)
        return get_prodcts()


if __name__ == '__main__':
    search()


