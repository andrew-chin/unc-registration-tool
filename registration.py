from selenium import webdriver
from webbrowser import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sqlite3
import pandas as pd
import random


def get_text_otp():
    conn = sqlite3.connect("/Users/{youruser}/Library/Messages/chat.db")

    messages = pd.read_sql_query("select * from message order by ROWID desc limit 1", conn)
    handles = pd.read_sql_query("select * from handle order by ROWID desc limit 1", conn)

    messages.rename(columns={'ROWID': 'message_id'}, inplace=True)
    handles.rename(columns={'id': 'phone_number', 'ROWID': 'handle_id'}, inplace=True)
    imessage_df = pd.merge(messages[['text', 'handle_id', 'date', 'is_sent', 'message_id']],
                           handles[['handle_id', 'phone_number']], on='handle_id', how='left')

    for index, row in imessage_df.iterrows():
        if row['handle_id'] == #print handles and find the id of DUO}:
            verification_code_text = row['text']
            for i in range(0, len(verification_code_text)):
                if verification_code_text[i] == ':':
                    return verification_code_text[i + 2:]
            
        else:
            print("verification code not found")
            return None

    return "Some error occurred"

print(get_text_otp())
options = Options()
options.add_experimental_option("detach", True)

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

driver.get("https://connectcarolina.unc.edu/")

links = driver.find_elements("xpath", "//a[@href]")


for link in links:
    if "Log In" in link.get_attribute("innerHTML"):
        link.click()
        break

driver.maximize_window()
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
element = driver.find_element("id", "username")
element.send_keys('{username{')
button = driver.find_element("id", "nextBtn")
button.click()
element = driver.find_element("id", "password")
element.send_keys('{password}')
button = driver.find_element("id", "submitBtn")
button.click()
driver.implicitly_wait(30)
driver.find_element("class name", "button--primary--full-width").click()
time.sleep(10)
otp = get_text_otp()
driver.find_element("id", "passcode-input").send_keys(otp)
driver.find_element("class name", "c--primary").click()
driver.find_element("id", "trust-browser-button").click()

driver.implicitly_wait(40)
time.sleep(5)
driver.get("https://pa.cc.unc.edu/psp/paprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?A=1")

test = 0
driver.implicitly_wait(5)
iframe = driver.find_element("xpath", "//iframe[@id = 'ptifrmtgtframe']")

driver.switch_to.frame(iframe)
counter = 0
while test == 0:
    driver.find_element("xpath", "//input[@value = 'Proceed to Step 2 of 3']").click()
    driver.implicitly_wait(5)
    driver.find_element("xpath", "//input[@value = 'Finish Enrolling']").click()
    driver.implicitly_wait(5)
    driver.find_element("xpath", "//input[@value = 'Add Another Class']").click()
    counter += 1
    print("Tried for " + str(counter) + " time")
    print("COMP 311: " + driver.find_element("id", "win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$0").text)
    print("COMP 421: " + driver.find_element("id", "win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$1").text)
    print("MATH 347: " + driver.find_element("id", "win0divDERIVED_REGFRM1_SS_MESSAGE_LONG$2").text)
    time.sleep(random.randint(40, 60))


