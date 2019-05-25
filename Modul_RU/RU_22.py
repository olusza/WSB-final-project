
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from faker.providers import internet
import time

def RU_22(driver, use_time_sleep=False):

	# Hasło cztery spacje i jedna liter kolejno na poczatku, w środku i na końcu.

	
	wait = WebDriverWait(driver, 10)
	fake = Faker('pl_PL')
	haslo_moje=["a    ", "  a  ", "    a"]
	Test_wynik_pozytywny=0
	Test_wynik_negatywny=0
	kod_grupy="wsbpsto2019"

	for i in range(0,3):

		driver.get('http://kmg.hcm.pl/testowanie/register.html')
		login=driver.find_element_by_id('username')
		login.send_keys(fake.user_name())


		haslo=driver.find_element_by_id('pass1')	
		haslo.send_keys(haslo_moje[i])

		haslo_powtorz=driver.find_element_by_id('pass2')
		haslo_powtorz.send_keys(haslo_moje[i])

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

		print("Test RU_05_chrome hasła: \"" + str(haslo_moje[i]) + "\" zakończony wynikiem ", end='')

		if "REJESTRACJA" in komentarz.upper() :
			print("pozytywnym.")
			Test_wynik_pozytywny+=1
		else:
			print("negatywnym.")
			Test_wynik_negatywny+=1

	print("Wynik pozytywny= " + str(Test_wynik_pozytywny))
	print("Wynik negatywny= " + str(Test_wynik_negatywny))	
		
	driver.quit()

