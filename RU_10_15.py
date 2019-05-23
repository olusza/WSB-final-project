# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def RU_10_15(driver, use_time_sleep=False):

	# Pozostawione puste kolejne pola w formularzu rejestracji.

	wait = WebDriverWait(driver, 10)

	Test_wynik_pozytywny=0
	Test_wynik_negatywny=0

	dane=["", "izunia", "izunia", "Ola", "Kaczor", "wsbpsto2019"]

	log=["", "haslo", "powtorz_haslo", "imie", "nazwisko", "kod_grupy"]

	for i in range(0,6):

		dane2=dane.copy()
		dane2[i] = ""

		driver.get('http://kmg.hcm.pl/testowanie/register.html')

		login=driver.find_element_by_id('username')
		login.send_keys(log[i])


		haslo=driver.find_element_by_id('pass1')
		haslo.send_keys(dane2[1])

		haslo_powtorz=driver.find_element_by_id('pass2')
		haslo_powtorz.send_keys(dane2[2])

		imie=driver.find_element_by_id('name')
		imie.send_keys(dane2[3])

		nazwisko=driver.find_element_by_id('surname')
		nazwisko.send_keys(dane2[4])

		kod=driver.find_element_by_id('kodgrupy')
		kod.send_keys(dane2[5])

		przycisk=driver.find_element_by_id('register')
		przycisk.click()

		if use_time_sleep:
			time.sleep(1)
		rejestracja = wait.until(EC.visibility_of_element_located((By.ID, 'registerCom')))
		komentarz=rejestracja.text

		if i==0:
			log[i]="login"

		print("Test w polu: \"" + log[i] + "\" zakończony wynikiem", end='')

		if "WSZYSTKICH" in komentarz.upper():
			print(" pozytywnym.")
			Test_wynik_pozytywny+=1
		else:	
			print(" negatywnym.")
			Test_wynik_negatywny+=1

	print("Wynik pozytywny= " + str(Test_wynik_pozytywny))
	print("Wynik negatywny= " + str(Test_wynik_negatywny))
	driver.quit()


