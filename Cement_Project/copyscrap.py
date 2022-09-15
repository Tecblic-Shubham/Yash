import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from xlwt import Workbook
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
 
#ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

wb = Workbook()
sheet = wb.add_sheet('Sheet 2')
felement_count = 0


ff_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

ff_driver.get("https://housing.com/in/buy/searches/AB0AE0P4hkd3fsj8fd9kanb")
felement = ff_driver.find_elements(By.CLASS_NAME,"css-zxue4u")
time.sleep(10)
for i in felement:
        felement_count += 1
        #ff_driver.switch_to.window(ff_driver.window_handles[0])
        i.click()
        time.sleep(10)
        #ff_driver.switch_to.window(ff_driver.window_handles[1])
        #Title = ff_driver.find_elements(By.CLASS_NAME,"proj-info__data__title")
        #Data = ff_driver.find_elements(By.CLASS_NAME,"proj-info__data__value")
        #try:
         #   Heading = ff_driver.find_element(By.CLASS_NAME,"heading")
          #  sheet.write(felement_count,0,str(Heading.text))
        #except:
         #   print("NO")
        #for (k,j) in zip(Title,Data):
         #       print(k.text)
          #      if(k.text=="Status"):
           #         sheet.write(felement_count,1,str(j.text))  
            #        print(f"Added {j.text} in Status")
             #   elif(k.text=="Price per Sqft"):
              #      sheet.write(felement_count,2,str(j.text))
               #     print(f"Added {j.text} in Price per Sqft")
                #elif(k.text=="Launch Date"):
                 #   sheet.write(felement_count,3,str(j.text))
                  #  print(f"Added {j.text} in Launch Date")
               # elif(k.text=="Possession by"):
                #    sheet.write(felement_count,4,str(j.text))
                #    print(f"Added {j.text} in Possession by")
                #elif(k.text=="Total Units"):
                 #   sheet.write(felement_count,5,str(j.text))
                  #  print(f"Added {j.text} in Total Units")
    #            elif(k.text=="Total Towers"):
     #               sheet.write(felement_count,6,str(j.text))
      #              print(f"Added {j.text} in Total Towers")
       #         elif(k.text=="Project Type"):
        #            sheet.write(felement_count,7,str(j.text))
         #           print(f"Added {j.text} in Project Type")
          #      elif(k.text=="Property Type"):
           #         sheet.write(felement_count,8,str(j.text))
            #        print(f"Added {j.text} in Property Type")
             #   elif(k.text=="Project Area"):
              #      sheet.write(felement_count,9,str(j.text))
               #     print(f"Added {j.text} in Project Area")
                #elif(k.text=="Full Address"):
                 #   sheet.write(felement_count,10,str(j.text))
                 #   print(f"Added {j.text} in Full Address")
    #            elif(k.text=="Pincode"):
     #               sheet.write(felement_count,11,str(j.text))
     #               print(f"Added {j.text} in Pincode")
     #           else:
      #              print("NO")
    
        #ff_driver.close()
wb.save('/home/tecblic/Desktop/Projects/Cement_Project/housing_new.xlsx')
ff_driver.quit()