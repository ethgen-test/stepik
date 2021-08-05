from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x_element= browser.find_element_by_css_selector ('#input_value')
    x=x_element.text
    y=calc(x) 

    text_field1=browser.find_element_by_css_selector ('.form-control')
    text_field1.send_keys(y)

    check_box11 = browser.find_element_by_css_selector("#robotCheckbox")
    check_box11.click()
    radio1=browser.find_element_by_css_selector("#robotsRule")
    radio1.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
