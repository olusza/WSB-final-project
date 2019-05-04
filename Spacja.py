# -*- coding: utf-8 -*-


from selenium import webdriver
driver = webdriver.Chrome()
import time
Test_wynik_pozytywny=0
Test_wynik_negatywny=0
driver.get('http://kmg.hcm.pl/testowanie/register.html')

dane="izunia", "izunia", "Ola", "Kaczor", "wsbpsto2019"]

log=["login", "haslo", "powtorzhaslo", "imie", "nazwisko"]
haslo=[]

for i in range(0,6):

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
	rejestracja=driver.find_element_by_id('registerCom')
	komentarz=rejestracja.text
	if "WSZYSTKICH" in komentarz :
		print("Test zakończony wynikiem pozytywnym " + element)
		Test_wynik_pozytywny+=1
	else:
		print("Test zakończony wynikiem negatywnym " + element)
		Test_wynik_negatywny+=1
print("Wynik pozytywny= " + str(Test_wynik_pozytywny))
print("Wynik negatywny= " + str(Test_wynik_negatywny))
driver.quit()



