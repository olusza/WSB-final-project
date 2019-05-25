# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def RU_17_20(driver, use_time_sleep=False):

	# 5 spacji w polach formularza: "login", "imię", "nazwisko". "kod grupy".

	wait = WebDriverWait(driver, 10)

	Test_wynik_pozytywny=0
	Test_wynik_negatywny=0

	dane=["     ", "Ola", "Kaczor", "wsbpsto2019"]

	log=["     ", "imie_17_20", "nazwisko_17_20", "kod_grupy_17_20"]

	for i in range(0,4):

		dane2=dane.copy()
		dane2[i] = "     "

		driver.get('http://kmg.hcm.pl/testowanie/register.html')

		login=driver.find_element_by_id('username')
		login.send_keys(log[i])


		haslo=driver.find_element_by_id('pass1')
		haslo.send_keys("aaaaa")

		haslo_powtorz=driver.find_element_by_id('pass2')
		haslo_powtorz.send_keys("aaaaa")

		imie=driver.find_element_by_id('name')
		imie.send_keys(dane2[1])

		nazwisko=driver.find_element_by_id('surname')
		nazwisko.send_keys(dane2[2])

		kod=driver.find_element_by_id('kodgrupy')
		kod.send_keys(dane2[3])

		przycisk=driver.find_element_by_id('register')
		przycisk.click()

		if use_time_sleep:
			time.sleep(1)
		rejestracja = wait.until(EC.visibility_of_element_located((By.ID, 'registerCom')))
		komentarz=rejestracja.text

		if i==0:
			log[i]="login_17_20"

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


