from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://eadigital.emdi.online/")

time.sleep(3)

navegador.find_element_by_xpath('//*[@id="controls"]/div/form/div[3]/input').send_keys("demo@demo.com")

time.sleep(1)

navegador.find_element_by_xpath('//*[@id="controls"]/div/form/div[4]/input').send_keys("123456")

time.sleep(2)

navegador.find_element_by_xpath('//*[@id="submit"]').click()

time.sleep(8)

navegador.find_element_by_xpath('//*[@id="navigation-example"]/div/div[2]/ul/li/a/i').click()

time.sleep(5)

navegador.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div/div/center/a[1]').click()