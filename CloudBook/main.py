import undetected_chromedriver.v2 as uc
import os, time
from selenium.webdriver.common.by import By
import socket
from selenium.webdriver.common.keys import Keys


if __name__=="__main__":

       options = uc.ChromeOptions()

       socket.getaddrinfo('localhost', 8080)

       acc = int(input("Enter number of loops :  "))
              
       password = ()
       username = ()
              #fullname = random_char(6) + " " + random_char(7)
       driver = uc.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe")
              #sdriver = webdriver.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe")
       driver.maximize_window()

       driver.get("https://www.cloudbooksapp.com/app/index.html#invoice")
       os.system('cls')
       time.sleep(3)
              #btc = driver.find_element(By.xpath(".click-to-copy")).click()
              #driver.find_element(By.XPATH, "//*[@class='section-btn-header']/div/div/div/button[1]/span/select").click()
              
       #email
       email=driver.find_element(By.ID, "inputEmail")
       email.send_keys(username)
       time.sleep(1)
       #password
       driver.find_element(By.ID, "inputPassword").send_keys(password)
       time.sleep(1)
       driver.find_element(By.XPATH, "//*[@class='tac mtop10']/button").click()
       time.sleep(10)

       #billing
       driver.find_element(By.XPATH, "(//*[@class='navbar-nav'])[2]/li[4]/a").click()
       time.sleep(1)

       #invoice
       driver.find_element(By.XPATH, "(//*[@class='navbar-nav'])[2]/li[4]/div/ul/li[1]/a").click()
       time.sleep(8)

       #edit
       driver.find_element(By.XPATH, "//*[@class='card']/div[2]/table/tbody/tr[1]/td[8]/a").click()
       time.sleep(3)

       count=1
       run=1
       j=0
       k=1
       

       def send_all(count,acc,run,j,k):

              #emails
              file1=None
              filE1=None
              read1=None
              set1=None
              set2=None
              main_file=None
              
              driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[1]/input[1]").clear()
              time.sleep(1)

              file1=open('E1.txt','r')
              filE1=open('S1.txt','a')
              read1=file1.readlines()[0:5]
              for line in read1:
                     kk= line.strip()
                     driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[1]/input[1]").send_keys(kk)
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

              file1=None
              filE1=None
              read1=None
              set1=None
              set2=None
              main_file=None

              file1=open('E2.txt','r')
              filE1=open('S2.txt','a')
              read1=file1.readline()
              
              driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[1]/input[1]").send_keys(read1)
              time.sleep(0.5)

              filE1.writelines(read1)
              file1.close()
              filE1.close()
              with open("E2.txt") as filE1:
                     set1 = set(filE1.readlines())
              with open("S2.txt") as filE1:
                     set2 = set(filE1.readlines())
              main_file = set1-set2
              with open("E2.txt","w") as file1:
                     file1.writelines(main_file)
              file1.close()
              time.sleep(1)
              #update invoice
              driver.find_element(By.XPATH, "(//*[@class='row mtop20'])[2]/div/button").click()
              time.sleep(5)

              #ok
              driver.find_element(By.XPATH, "(//*[@class='modal-footer'])[6]/button").click()
              time.sleep(2)

              #send by email
              driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div/div/a[3]").click()
              time.sleep(1)

              #ok
              driver.find_element(By.XPATH, "(//*[@class='modal-footer'])[6]/button").click()
              time.sleep(2)

              if k<=4:
                     #edit invoice
                     driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div/div/a[1]").click()
                     time.sleep(5)
              else:
                     k=0
                     try:
                            #invoice
                            driver.find_element(By.XPATH, "(//*[@class='navbar-nav'])[2]/li[4]/div/ul/li[1]/a").click()
                            time.sleep(3)
                     except:
                            #billing
                            driver.find_element(By.XPATH, "(//*[@class='navbar-nav'])[2]/li[4]/a").click()
                            time.sleep(1)

                            #invoice
                            driver.find_element(By.XPATH, "(//*[@class='navbar-nav'])[2]/li[4]/div/ul/li[1]/a").click()
                            time.sleep(3)

                     #New Invoice
                     driver.find_element(By.XPATH, "//*[@class='row align-items-end']/div[3]/div/a").click()
                     time.sleep(5)

                     #customer
                     driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[1]/div[1]/input").send_keys("Customer")
                     time.sleep(0.5)
                     driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[3]/div[1]/input").click()
                     time.sleep(0.5)
                     
                     #emails
                     file1=None
                     filE1=None
                     read1=None
                     set1=None
                     set2=None
                     main_file=None
                     
                     driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[1]/input[1]").clear()
                     time.sleep(1)

                     file1=open('E1.txt','r')
                     filE1=open('S1.txt','a')
                     read1=file1.readlines()[0:5]
                     for line in read1:
                            kk= line.strip()
                            driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div[3]/div[1]/input[1]").send_keys(kk)
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

                     #items
                     driver.find_element(By.XPATH, "//*[@class='row mtop20']/div/div[1]/table/tbody/tr[1]/td[1]/input[2]").send_keys("Product and Services")
                     time.sleep(1)
                     
                     #send Emails
                     driver.find_element(By.XPATH, "//*[@class='col-12 mb20 tac ftrbtn']/button[2]").click()
                     time.sleep(4)

                     #message
                     if j<9:
                            j=j+1
                     else:
                            j=1
                     file1=None
                     read1=None
                     main_file=None

                     file1=open(f'message ({j}).txt','r')
                     read1=file1.readlines()
                     driver.find_element(By.XPATH, "(//*[@class='note-editor note-frame card'])[3]/div[3]/div[2]").clear()
                     driver.find_element(By.XPATH, "(//*[@class='note-editor note-frame card'])[3]/div[3]/div[2]").send_keys(read1)
                     file1.close()
                     time.sleep(1)
              
                     #attached pdf
                     driver.find_element(By.XPATH, "(//*[@class='reminder_left'])[3]/input").click()
                     time.sleep(0.5)

                     #send
                     driver.find_element(By.XPATH, "(//*[@class='popfoot'])/button[1]").click()
                     time.sleep(8)

                     #edit invoice
                     driver.find_element(By.XPATH, "(//*[@class='container-fluid'])[2]/div[1]/div/div/a[1]").click()
                     time.sleep(5)


                                   

              k=k+1
              print("sent=",count)
              count=count+1
              time.sleep(1)
              #------------------------------------------------------------------------------------------------------

              if run<acc:
                     run=run+1
                     send_all(count,acc,run,j,k)
              else:
                     driver.quit()

       send_all(count,acc,run,j,k)