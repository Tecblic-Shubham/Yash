import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://dev.thesciencepark.dev/")

from webdriver_manager.firefox import GeckoDriverManager
 
ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
ff_driver.get("https://dev.thesciencepark.dev/")

from webdriver_manager.microsoft import EdgeChromiumDriverManager

oo_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
oo_driver.get("https://dev.thesciencepark.dev/")
time.sleep(10)

driver.quit()
ff_driver.quit()
oo_driver.quit()