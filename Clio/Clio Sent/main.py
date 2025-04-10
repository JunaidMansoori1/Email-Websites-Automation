import undetected_chromedriver.v2 as uc
import os, time
from selenium.webdriver.common.by import By
import socket
from selenium.webdriver.common.keys import Keys


if __name__=="__main__":

       options = uc.ChromeOptions()

       # options.add_argument("--user-data-dir="Enter your Google Chrome Profile Directory")

       socket.getaddrinfo('localhost', 8080)

       acc = int(input("Enter number of loops :  "))
              
       password = ()
       username = ()
              #fullname = random_char(6) + " " + random_char(7)
       driver = uc.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe")
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

       #Billing
       # driver.find_element(By.XPATH, "//*[@class='nav-container']/li[8]/a").click()
       # time.sleep(2)

       
       count=1
       run=1
       j=0
       

       def send_all(count,acc,run,j):

              #Send
              driver.find_element(By.XPATH, "//*[@class='th-combo-button-basic']/button[1]").click()
              time.sleep(2.5)

              #email
              driver.find_element(By.XPATH, "//*[@class='k-multiselect-wrap k-floatwrap']/input").clear()

              # for i in range(50):
              file1=None
              filE1=None
              read1=None
              set1=None
              set2=None
              main_file=None

              file1=open('E1.txt','r')
              filE1=open('S1.txt','a')
              read1=file1.readlines()[0:50]
              for line in read1:
                     kk= line.strip()
                     try:
                            driver.find_element(By.XPATH, "//*[@class='k-multiselect-wrap k-floatwrap']/input").send_keys(kk)
                            time.sleep(1)
                            driver.find_element(By.XPATH, "//*[@class='k-list-container k-popup k-group k-reset k-state-border-up']/div[2]/ul/li").click()
                            time.sleep(0.5)
                     except:
                            time.sleep(1)
                            driver.find_element(By.XPATH,"//*[@class='share-from-info spacing-stack-l']/th-disclosure-toggle/a").click()
                            time.sleep(0.5)
              
              
              #send bill
              driver.find_element(By.XPATH, "//*[@class='modal-actions']/ng-transclude/th-button-group/th-button[1]/button").click()
              time.sleep(0.5)

              filE1.writelines(read1)
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
              time.sleep(1)

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