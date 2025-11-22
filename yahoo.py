import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from supabase import create_client, Client

'''
pip install requests selenium supabase

python yahoo_supa.py
'''

url_ = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"

supabase: Client = create_client(url_, key)

def main():
    thus_1 = True
    while thus_1:
        thus_2 = True
        while thus_2:
            profile_dir = tempfile.mkdtemp()
            try:
                chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
                chromedriver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
                
                options = Options()
                options.binary_location = chrome_bin
                options.add_argument("--headless")
                options.add_argument(f"--user-data-dir={profile_dir}")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
                
                #url ="https://signup.live.com/signup?cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&id=292841&contextid=53955DF24C88E866&opid=4B9EF33C96C27BF8&bk=1725636660&sru=https://login.live.com/login.srf%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26id%3d292841%26contextid%3d53955DF24C88E866%26opid%3d4B9EF33C96C27BF8%26mkt%3dEN-US%26lc%3d1033%26bk%3d1725636660%26uaid%3d1e6edfe7c20e484684dd1799a3c93f43&lw=dob,flname,wld&fl=1&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=1e6edfe7c20e484684dd1799a3c93f43"
                url ="https://login.yahoo.com/account/challenge/username?done=https%3A%2F%2Fwww.yahoo.com%2F&authMechanism=secondary&chllngnm=fail&sessionIndex=Qg--"
                driver.get(url)
                time.sleep(3)
                
                a=driver.find_elements(By.TAG_NAME, "a")
                for link in a:
                    if 'over' in link.get_attribute('innerText') or 'Recommencer' in link.get_attribute('innerText'):
                        link.click()
                        time.sleep(2)
                        break       
                table_name = "yahoo_de"
                while True:
                    response_data_3 = supabase.rpc(
                        "select_before_and_after_update_yahoo",
                        {"uid": 1, "new_name": table_name}
                    ).execute()
                    
                    a=driver.find_elements(By.TAG_NAME, "a")
                    for link in a:
                        if 'over' in link.get_attribute('innerText') or 'Recommencer' in link.get_attribute('innerText'):
                            link.click()
                            time.sleep(2)
                            break
                    
                    em = str(response_data_3.data[0]['email'])
                    id = response_data_3.data[0]['id']
                    try:
                        na_me=driver.find_element(By.NAME, "username")
                        na_me.clear()
                        na_me.send_keys(em)
                    except:
                        url ="https://login.yahoo.com/account/challenge/username?done=https%3A%2F%2Fwww.yahoo.com%2F&authMechanism=secondary&chllngnm=fail&sessionIndex=Qg--"
                        driver.get(url)
                        time.sleep(3)
                        
                        a=driver.find_elements(By.TAG_NAME, "a")
                        for link in a:
                            if 'over' in link.get_attribute('innerText') or 'Recommencer' in link.get_attribute('innerText'):
                                link.click()
                                time.sleep(2)
                                break   
                        na_me=driver.find_element(By.NAME, "username")
                        na_me.clear()
                        na_me.send_keys(em) 

                    verifyYid=driver.find_element(By.NAME, "verifyYid")
                    verifyYid.click()
                    current_url = driver.current_url
                    if 'account/challenge/email-verify?done=' in current_url:
                        try:
                            response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "yes"}).eq("id", id).execute()
                            response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                            print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                            print('yes: ', em)
                        except:
                            pass
                        driver.back()
                        time.sleep(2)
                        
                    elif 'account/challenge/pwqa?done=' in current_url:
                        try:
                            response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "yes"}).eq("id", id).execute()
                            response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                            print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                            print('yes: ', em)
                        except:
                            pass
                        driver.back()
                        time.sleep(2)
                        
                    elif 'account/challenge/challenge-selector?done=' in current_url:
                        try:
                            response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "yes"}).eq("id", id).execute()
                            response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                            print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                            print('yes: ', em)
                        except:
                            pass
                        driver.back()
                        time.sleep(2)
                        
                    elif 'account/challenge/username?done=' in current_url:
                        try:
                            response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "no"}).eq("id", id).execute()
                            response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                            print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                            print('no: ', em)
                        except:
                            pass
                        
                    elif 'recaptcha' in current_url:
                        try:
                            response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "yes"}).eq("id", id).execute()
                            response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                            print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                            print('yes: ', em)
                        except:
                            pass
                        driver.back()
                        time.sleep(2)
                    elif 'fail' in current_url:
                        try_devices = driver.find_elements(By.CLASS_NAME, "writeup")
                        if len(try_devices) > 0:
                            if 'device' in try_devices[0].get_attribute('innerText') or 'connecté' in try_devices[0].get_attribute('innerText'):
                                try:
                                    response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "yes"}).eq("id", id).execute()
                                    response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                                    print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                                    print('yes: ', em)
                                except:
                                    pass
                            else:
                                try:
                                    response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "no"}).eq("id", id).execute()
                                    response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                                    print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                                    print('no: ', em)
                                except:
                                    pass
                                
                        driver.back()
                        time.sleep(2)
                        a=driver.find_elements(By.TAG_NAME, "a")
                        for link in a:
                            if 'over' in link.get_attribute('innerText'):
                                link.click()
                                time.sleep(2)
                                break
                    else:
                        try:
                            response_data_3 = supabase.table(table_name).update({"status":"finished", "valid": "no"}).eq("id", id).execute()
                            response_data_3 = supabase.table(table_name).select("id, emails, status, valid").eq("id", id).execute()
                            print(f"valid  -> {str(id)}: ", response_data_3.data[0]['valid'])
                            print('no: ', em)
                        except:
                            pass
                            
                        driver.back()
                        time.sleep(2)
                        a=driver.find_elements(By.TAG_NAME, "a")
                        for link in a:
                            if 'over' in link.get_attribute('innerText'):
                                link.click()
                                time.sleep(2)
                                break
                driver.quit()
                driver.close()
                driver.dispose()
                shutil.rmtree(profile_dir, ignore_errors=True)
            except:
                shutil.rmtree(profile_dir, ignore_errors=True)
                print('err: ')

        print('Fin')

if __name__ == "__main__":
    main()
