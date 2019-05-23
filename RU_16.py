
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from faker.providers import internet
import time

def RU_16(driver, use_time_sleep=False):

	# Błędny kod grupy.

	
	wait = WebDriverWait(driver, 10)
	fake = Faker('pl_PL')
	kod_grupy="abcde"

	driver.get('http://kmg.hcm.pl/testowanie/register.html')

	login=driver.find_element_by_id('username')
	login.send_keys(fake.user_name())


	haslo=driver.find_element_by_id('pass1')	
	haslo.send_keys(fake.password(6))

	haslo_powtorz=driver.find_element_by_id('pass2')
	haslo_powtorz.send_keys(haslo.get_attribute("value"))

	imie=driver.find_element_by_id('name')
	imie.send_keys(fake.first_name())

	nazwisko=driver.find_element_by_id('surname')
	nazwisko.send_keys(fake.last_name())

	kod=driver.find_element_by_id('kodgrupy')
	kod.send_keys(kod_grupy)

	przycisk=driver.find_element_by_id('register')
	przycisk.click()

	if use_time_sleep:
		time.sleep(1)

	rejestracja = wait.until(EC.visibility_of_element_located((By.ID, 'registerCom')))
	komentarz=rejestracja.text

	if "REJESTRACJA" in komentarz.upper() :
		print("negatywnym.")
	
	else:
		print("pozytywnym.")
	
	driver.quit()

