import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C://Users//Prudvi Narendra//Downloads//chromedriver")
driver.get('https://www.facebook.com')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('jamesbondOO7')
act = ActionChains(driver)
act.key_down(Keys.COMMAND)
act.send_keys('A')
act.key_up(Keys.COMMAND)
act.perform()
act.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()
time.sleep(5)
driver.minimize_window()

#driver.execute_script("window.open('https://google.com')")
#driver.switch_to.window(driver.window_handles[1])
#act.click(driver.find_element_by_name('q')).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).send_keys(Keys.ENTER).perform()