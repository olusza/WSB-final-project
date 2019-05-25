from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def LG_01(driver):

	wait=WebDriverWait(driver, 3)
	login_moj="januszek"
	haslo_moje="jankowalski"
	
	driver.get('http://kmg.hcm.pl/testowanie/')

	login=driver.find_element_by_id('userLogin')

	login.send_keys(login_moj)

	haslo=driver.find_element_by_id('passwordLogin')
	haslo.send_keys(haslo_moje)

	driver.execute_script("element = document.querySelector('#login'); element.click()")

	try:
		wait.until(EC.alert_is_present())
		print(" negatywnym.")
	except TimeoutException:
		print(" pozytywnym.")

	driver.quit()