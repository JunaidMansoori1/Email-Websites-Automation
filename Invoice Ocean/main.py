import undetected_chromedriver as uc
from selenium import webdriver
import os, time
from selenium.webdriver.common.by import By
import socket
from selenium.webdriver.common.keys import Keys
import psutil
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__=="__main__":

       options = uc.ChromeOptions()
       options.add_argument("--incognito")
       # options.add_argument("--headless")
       # options.add_argument("--user-data-dir=C:\\Users\\Junaid\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

       socket.getaddrinfo('localhost', 8080)

       acc = int(input("Enter number of loops :  "))
              
       password = ('quousemmacrifoi-5523@yopmail.com')
       username = ('quousemmacrifoi-5523@yopmail.com')
              #fullname = random_char(6) + " " + random_char(7)
       driver = uc.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe",options=options)
       # driver = webdriver.Chrome(executable_path="d:\\chromedriver_win32\\chromedriver.exe", options=options)
       driver.set_window_size(500, 500)
       # driver.execute_script("document.body.style.zoom='33%'")


       driver.get("https://customerteam.invoiceocean.com/invoices")
       os.system('cls')
       time.sleep(1)
       driver.execute_script("document.body.style.zoom='33%'")
       time.sleep(3)
              #btc = driver.find_element(By.xpath(".click-to-copy")).click()
              #driver.find_element(By.XPATH, "//*[@class='section-btn-header']/div/div/div/button[1]/span/select").click()
       
       driver.execute_script("document.body.style.zoom='33%'")

       #email
       email=driver.find_element(By.XPATH,"(//*[@class='form-control'])[1]")
       email.send_keys(username)
       time.sleep(1)
       #password
       driver.find_element(By.XPATH, "(//*[@class='form-control'])[2]").send_keys(password)
       time.sleep(1)
       driver.find_element(By.XPATH, "//*[@class='btn-glow primary login']").click()
       time.sleep(3)
       driver.execute_script("document.body.style.zoom='33%'")
       time.sleep(7)

       count=1
       run=1
       j=0
       k=1

       

       def send_all(count,acc,run,j,k):

              global driver
              

              #client emails
              file1=None
              filE1=None
              read1=None
              set1=None
              set2=None
              main_file=None
              
              

              try:
                     # Wait for the element to be clickable
                     email_to = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='invoice_email_to']")))

                     # Scroll into view (if needed)
                     driver.execute_script("arguments[0].scrollIntoView();", email_to)

                     # Click the element
                     email_to.click()
              
              # driver.find_element(By.XPATH, "//*[@id='invoice_email_to']").click()
              # time.sleep(1)
              # driver.find_element(By.XPATH, "//*[@id='invoice_email_to']").clear()
              # time.sleep(1)
              # # driver.find_element(By.XPATH, "//*[@id='send']/form/div[3]/div[1]/select/option[3]").click()
              # # time.sleep(1)
              except:
                     time.sleep(5)
                     driver.find_element(By.XPATH, "//*[@id='send']/form/div[3]/div/input").clear()
                     time.sleep(0.5)

              file1=open('E1.txt','r')
              filE1=open('S1.txt','a')
              read1=file1.readlines()[0:5]
              for line in read1:
                     kk= line.strip()
                     driver.find_element(By.XPATH, "//*[@id='send']/form/div[3]/div/input").send_keys(kk)
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

              #CC
              file1=None
              filE1=None
              read1=None
              set1=None
              set2=None
              main_file=None
              driver.find_element(By.XPATH, "//*[@id='send']/form/div[4]/div/input").clear()
              file1=open('E1.txt','r')
              filE1=open('S1.txt','a')
              read1=file1.readlines()[0:5]
              for line in read1:
                     kk= line.strip()
                     # driver.find_element(By.XPATH, "//*[@id='send']/form/div[4]/div/input").clear()
                     driver.find_element(By.XPATH, "//*[@id='send']/form/div[4]/div/input").send_keys(kk)
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
       

              #Subject
              
              file1=None
              file2=None
              read1=None
              main_file=None

              # Open and read the first subject line
              with open('subject.txt', 'r', encoding="utf-8") as file1:
                     lines = file1.readlines()

              read1 = lines[0].strip()
              
              driver.find_element(By.XPATH, "//*[@id='send']/form/div[5]/div/input").clear()
              time.sleep(0.5)
              driver.find_element(By.XPATH, "//*[@id='send']/form/div[5]/div/input").send_keys(read1)
              time.sleep(1)
              
              # Add subject to S2.txt if it's not already there
              with open('S2.txt', 'r+', encoding="utf-8") as filE1:
                     file2 = set(filE1.read().splitlines())  # Read all lines as a set
              if read1 not in file2:
                     with open('S2.txt', 'a', encoding="utf-8") as filE1:
                            filE1.write(read1 + "\n")  # Add a newline after writing

              # Remove the used subject from subject.txt
              with open('subject.txt', 'w', encoding="utf-8") as file1:
                     file1.writelines(lines[1:])  # Write back all lines except the first one

              time.sleep(1)

              #message

              if j<5:
                     j=j+1
              else:
                     j=1


              file1=None
              read1=None
              main_file=None

              file1=open(f'message {j}.txt','r',encoding="utf-8")
              read1=file1.readlines()
              text_area = driver.find_element(By.XPATH, "//*[@id='send']/form/div[6]/div/textarea")
              text_area.click()
              time.sleep(0.5)
              text_area.clear()
              time.sleep(0.5)
              driver.execute_script("arguments[0].value = arguments[1];", text_area, "".join(read1))

              # text_area = driver.find_element(By.XPATH, "//*[@id='send']/form/div[6]/div/textarea")
              # text_area.click()
              # text_area.clear()
              # text_area.send_keys("".join(read1))
              # driver.find_element(By.XPATH, "//*[@id='send']/form/div[6]/div/textarea").clear()
              # driver.find_element(By.XPATH, "//*[@id='send']/form/div[6]/div/textarea").send_keys(read1)
              file1.close()
              time.sleep(2)
              
              #Send
              try:
                     driver.find_element(By.XPATH, "//*[@id='send']/form/div[8]/input").click()
                     time.sleep(5)
              except:
                     driver.find_element(By.XPATH, "//*[@id='send']/form/div[9]/input").click()
                     time.sleep(5)
              
              

              if k<=7:
                     #sent
                     driver.find_element(By.XPATH, "(//*[@class='collapse navbar-collapse navbar-ex1-collapse'])[1]/ul[1]/li[2]/a").click()
                     time.sleep(1)
              else:
                     k=0
                     #more option
                     driver.find_element(By.XPATH, "(//*[@class='collapse navbar-collapse navbar-ex1-collapse'])[1]/ul[1]/li[5]/a").click()
                     time.sleep(1)

                     #add similar
                     driver.find_element(By.XPATH, "(//*[@class='collapse navbar-collapse navbar-ex1-collapse'])[1]/ul[1]/li[5]/ul/li[1]/a").click()
                     time.sleep(5)


                     try:
                            #save
                            driver.find_element(By.XPATH, "//*[@id='buttons1']/a[1]").click()
                            time.sleep(5)
                     except:
                            time.sleep(3)
                            driver.find_element(By.XPATH, "//*[@id='buttons1']/a[1]").click()
                            time.sleep(5)

                     try:
                            #sent
                            driver.find_element(By.XPATH, "(//*[@class='collapse navbar-collapse navbar-ex1-collapse'])[1]/ul[1]/li[2]/a").click()
                            time.sleep(2)
                     except:
                            time.sleep(3)
                            driver.find_element(By.XPATH, "(//*[@class='collapse navbar-collapse navbar-ex1-collapse'])[1]/ul[1]/li[2]/a").click()
                            time.sleep(2)

                                   

              k=k+1
              # l=l+1
              print("sent=",count)
              count=count+1
              time.sleep(2)
                     

              



              #------------------------------------------------------------------------------------------------------

              if run<acc:
                     run=run+1
                     send_all(count,acc,run,j,k)
              else:
                     driver.quit()


       send_all(count,acc,run,j,k)