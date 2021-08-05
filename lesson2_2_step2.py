from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math

link="http://suninjuly.github.io/selects2.html"

try:

    browser=webdriver.Chrome()
    browser.get(link)
    num1=browser.find_element_by_css_selector('#num1')
    text_num1=int(num1.text)
    num2=browser.find_element_by_css_selector('#num2')
    text_num2=int(num2.text)
    summa=text_num1+text_num2
    print (summa)
    text=str(summa)
    print(text)
    select1=browser.find_element_by_css_selector('.custom-select')
    select1.click()
    browser.find_element_by_css_selector("option:nth-child(2)").click()
    
    browser.find_element_by_tag_name("button").click()



finally:

    time.sleep(10)
    browser.quit()
