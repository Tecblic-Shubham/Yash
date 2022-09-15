import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from xlwt import Workbook
from webdriver_manager.firefox import GeckoDriverManager
 
ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
ff_driver.get("https://www.magicbricks.com/")
time.sleep(10)
ff_driver.find_element(By.CLASS_NAME,"mb-search__tag-t").click()
ff_driver.find_element(By.CLASS_NAME,"mb-search__tag-close").click()
element = ff_driver.find_element(By.CLASS_NAME,"mb-search__input")
element.send_keys("Ahmedabad")
time.sleep(5)
ff_driver.find_element(By.CLASS_NAME,"mb-search__auto-suggest__item").click()
ff_driver.find_element(By.CLASS_NAME,"mb-search__btn").click()
time.sleep(5)
ff_driver.find_element(By.XPATH,"//*[@id='body']/div[4]/div/div/div[1]/div[3]/ul/li[2]/a").click()
time.sleep(5)
ff_driver.find_element(By.XPATH,"//*[@id='propTypekIco']").click()
time.sleep(5)
ff_driver.find_element(By.XPATH,"//*[@id='bedroomstkIco']").click()
time.sleep(5)
ff_driver.find_element(By.XPATH,"//*[@id='refineMoreTitle']").click()
time.sleep(5)
ff_driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div/div/div/div/div[9]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/label").click()
ff_driver.find_element(By.XPATH,"//*[@id='moreRefined']/div[3]/div[2]/div[2]").click()
time.sleep(5)
felement = ff_driver.find_elements(By.CLASS_NAME,"proHeading")
Location = ff_driver.find_elements(By.CLASS_NAME,"proGroup")
Size = ff_driver.find_elements(By.CLASS_NAME,"proDescColm2")
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
felement_count = 0
f2=open("/home/tecblic/Desktop/Projects/Cement_Project/output.xlsx",'w')
for i in felement:
    print(i.text)
    sheet1.write(felement_count,0,str(i.text))
    felement_count += 2
felement_count2 = 0
for i in Location:
    print(i.text)
    sheet1.write(felement_count2,1,str(i.text))
    felement_count2 += 1
felement_count3 = 0
for i in Size:
    print(i.text)
    sheet1.write(felement_count3,2,str(i.text))
    felement_count3 += 2
wb.save('/home/tecblic/Desktop/Projects/Cement_Project/output.xlsx')
ff_driver.quit()