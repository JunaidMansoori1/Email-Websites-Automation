# from selenium.webdriver import Chrome
from selenium import webdriver 
import os, time
from selenium.webdriver.common.by import By
import socket
from selenium.webdriver.common.keys import Keys


if __name__=="__main__":

       options = webdriver.ChromeOptions()

       options.add_argument("--user-data-dir=C:\\Users\\Junaid\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

       socket.getaddrinfo('localhost', 8080)

       acc = int(input("Enter number of loops :  "))
              
       password = ()
       username = ()
              #fullname = random_char(6) + " " + random_char(7)
       driver = webdriver.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe")
              #sdriver = webdriver.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe")
       driver.set_window_size(150,400)

       driver.get("https://app.clio.com/nc/#/bills")
       os.system('cls')
       time.sleep(3)
              #btc = driver.find_element(By.xpath(".click-to-copy")).click()
              #driver.find_element(By.XPATH, "//*[@class='section-btn-header']/div/div/div/button[1]/span/select").click()
              
       #email
       email=driver.find_element(By.ID,"email")
       email.send_keys(username)
       time.sleep(1)

       #next password
       driver.find_element(By.XPATH,"//*[@class='button-group']/button").click()
       time.sleep(3)

       #password
       pas=driver.find_element(By.ID,"password")
       pas.send_keys(password)
       time.sleep(1)
       driver.find_element(By.XPATH,"//*[@class='button-group']/input").click()
       time.sleep(20)

       
       count=1
       run=1
       j=0
       

       def send_all(count,acc,run,j):

              #contact
              driver.find_element(By.XPATH, "//*[@class='nav-container']/li[5]/a").click()
              time.sleep(2)
              #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form-table']/div[1]/div/div/div/div/div/div/div/div/div"))).click()
              
              #New Person
              driver.find_element(By.XPATH, "(//*[@class='right-aligned-content']/cc-page-header-right/th-button/button)[1]").click()
              time.sleep(2.5)

              #First Name
              file1=None
              filE1=None
              read1=None
              set1=None
              set2=None
              main_file=None

              file1=open('E1.txt','r')
              filE1=open('S1.txt','a')
              read1=file1.readline()
              driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[2]/label/span[2]/input").clear()
              # driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[2]/label/span[2]/input").click()
              driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[2]/label/span[2]/input").send_keys(read1)
              time.sleep(0.5)
              driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[4]/label/span[2]/input").clear()
              # driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[2]/label/span[2]/input").click()
              driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[4]/label/span[2]/input").send_keys(read1)
              time.sleep(0.5)
              driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[4]/th-column[1]/label/span[2]/input").clear()
              # driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[2]/th-column[2]/label/span[2]/input").click()
              driver.find_element(By.XPATH, "(//*[@class='row justify-content-start'])[4]/th-column[1]/label/span[2]/input").send_keys(read1)

              filE1.write(read1)
              file1.close()
              filE1.close()
              with open("E1.txt") as filE1:
                     set1 = set(filE1.readlines())
              with open("S1.txt") as filE1:
                     set2 = set(filE1.readlines())
              main_file = set1-set2
              with open("E1.txt","w") as file1:
                     file1.writelines(main_file)
              file1.close()
              time.sleep(0.5)
              
              #save Contact
              driver.find_element(By.XPATH, "(//*[@class='ml-auto mr-auto'])[1]/th-button[1]/button").click()
              time.sleep(0.5)

              print("sent=",count)
              count=count+1
              time.sleep(5)
              #------------------------------------------------------------------------------------------------------

              if run<acc:
                     run=run+1
                     send_all(count,acc,run,j)
              else:
                     driver.quit()

       send_all(count,acc,run,j)