from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "http://127.0.0.1:5000/emp"; 
driver.get(url)
#로딩되는 시간동안
#sleep(1)
trs = driver.find_elements(By.CSS_SELECTOR,"#test > tr")
#print(trs[2].text)
for i in trs:
    #test > tr:nth-child(2) > td:nth-child(1)
#    name = tr.find_elements(By.CSS_SELECTOR,"td")[1].text


    addr = i.find_elements(By.CSS_SELECTOR,"td")[1].text
    print(addr)
    #

    # print(tr.find_elements(By.CSS_SELECTOR,"td")[0].text)
    # print(tr.find_elements(By.CSS_SELECTOR,"td")[0].text)
    # print(tr.find_elements(By.CSS_SELECTOR,"td")[0].text)