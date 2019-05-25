import time

def LG_05(driver, use_time_sleep=False):

	# Poprawne działanie przycisku: "Rejestruj".
	
	driver.get('http://kmg.hcm.pl/testowanie/')

	driver.execute_script("document.querySelector(\"a[href='register.html']\").click()")

	if use_time_sleep:
		time.sleep(1)

	url=driver.current_url
	
	url_strony="/testowanie/register.html"

	if url_strony in url: 
		print(" pozytywnym.")
	else:
		print(" negatywnym.")

	driver.quit()


