from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import re
import time


browser = webdriver.Chrome() #声明浏览器并初始化
wait = WebDriverWait(browser, 10) #指定最长等待时间

def search():
    try:
        browser.get('https://www.jd.com') #访问页面
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key'))) #用until(传入要等待的条件：节点加载出来，传入定位元组，用CSS选择器)
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div.form > button'))) #用until(传入要等待的条件：节点可击，用CSS选择器)
        input.send_keys('美食') #节点交互：输入文字
        submit.click() #节点交互：点击按钮
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1)'))) #用until(传入要等待的条件：节点加载出来，传入定位元组，用CSS选择器)
        get_prodcts()
        return total.text
    except TimeoutError:
        return search()

def next_page(page_number):
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #利用execute_script()方法将进度条下拉到最底部
        time.sleep(10) #延时10是
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next'))
        )
        button.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(page_number))
        ) #判断是否翻页成功
        get_prodcts()
    except TimeoutError:
        return next_page(page_number)

#定义解析方法
def get_prodcts():
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList .gl-warp.clearfix .gl-item')))  #用until(传入要等待的条件：节点加载出来，传入定位元组，用CSS选择器)
        html = browser.page_source #获得网页源代码
        doc = pq(html) #选择pyquery并初始化
        items = doc('#J_goodsList .gl-warp.clearfix .gl-item .gl-i-wrap').items()
        for item in items:
            product = {
                'title': item.find('.p-name').text(),
                'image': item.find('.p-img img').attr('src'),
                'price': item.find('.p-price').text(),
                'commit': item.find('.p-commit').text(),
                'shop': item.find('.p-shop').text()
            }
            print(product)
    except TimeoutError:
        return get_prodcts()

def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, total - 88):
        next_page(i)


if __name__ == '__main__':
    main()