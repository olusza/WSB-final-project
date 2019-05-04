# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://kmg.hcm.pl/testowanie/')
login=driver.find_element_by_id('userLogin')
login.send_keys('amudyna')
haslo=driver.find_element_by_id('passwordLogin')
haslo.send_keys('sarka')
driver.execute_script("element = document.querySelector('#login'); element.click()")
time.sleep(1)
driver.execute_script("element = document.querySelector('[src=\"./icon_profile.png\"]'); element.click()")
time.sleep(1)
kilka_slow=driver.find_element_by_id('editOSobie')
kilka_slow.send_keys('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
driver.execute_script("element = document.querySelector('#editBttn'); element.click()")



