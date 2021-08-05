from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    picture1 = browser.find_element_by_id("treasure")
    picture_attr = picture1.get_attribute("valuex")
    
    y=calc(picture_attr)

    text_field=browser.find_element_by_id("answer")
    text_field.send_keys(y)
    flag=browser.find_element_by_id("robotCheckbox")
    flag.click()
    radio1=browser.find_element_by_id("robotsRule")
    radio1.click()
    button1=browser.find_element_by_css_selector('.btn.btn-default')
    button1.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
