from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import re
import time


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get('https://www.jd.com')
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div.form > button')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1)')))
        get_prodcts()
        return total.text
    except TimeoutError:
        return search()

def next_page(page_number):
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next'))
        )
        button.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(page_number))
        )
        get_prodcts()
    except TimeoutError:
        return next_page(page_number)


def get_prodcts():
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList .gl-warp.clearfix .gl-item')))
        html = browser.page_source
        doc = pq(html)
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

