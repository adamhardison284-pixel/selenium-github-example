from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from supabase import create_client, Client
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
    
    url = "https://jdnmanfimzvbilacjgcj.supabase.co"
    key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"
    supabase: Client = create_client(url, key)	
    
    response = supabase.table("gmail_smtps").select("*").execute()
    smtps = response.data
    
    options = Options()
    options.binary_location = chrome_bin
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    url = "https://sprintmail.ru/"
    for smtp in smtps:
        print('username: ', smtp['username'])
        if smtp['ready'] == True and smtp['checked'] == False:
            driver.get(url)
            thus = True
            while thus:
                user_inp = driver.find_element(By.ID, "webmail_username")
                user_pass = driver.find_element(By.ID, "webmail_pass")
                user_inp.send_keys(smtp['username'])
                user_pass.send_keys("Arbinaji1987$", Keys.ENTER)
                time.sleep(3)
                thus = False
                current_url = driver.current_url
                if "roundcubemail/?_task=mail&_mbox=INBOX" in current_url:
                    response_data_ = supabase.table('gmail_smtps').update({"ready": 1, "checked": 1}).eq("id", smtp['id']).execute()
                    driver.execute_script("document.getElementsByClassName('logout')[0].click()")
                    time.sleep(2)
                    print('username: yes'])
                else:
                    response_data_ = supabase.table('gmail_smtps').update({"ready": 0, "checked": 1}).eq("id", smtp['id']).execute()
                    print('username: no'])

if __name__ == "__main__":
    main()
