from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
from faker.providers import internet

def LG_03(driver):

	# Logowanie do konta poprawny login, błędne hasło.

	wait=WebDriverWait(driver, 3)
	fake=Faker('pl_PL')
	login_moj="januszek"
	
	driver.get('http://kmg.hcm.pl/testowanie/')

	login=driver.find_element_by_id('userLogin')
	login.send_keys(login_moj)

	haslo=driver.find_element_by_id('passwordLogin')
	haslo.send_keys(fake.password())

	driver.execute_script("element = document.querySelector('#login'); element.click()")

	try:
		wait.until(EC.alert_is_present())
		print(" pozytywnym.")
	except TimeoutException:
		print(" negatywnym.")

	driver.quit()