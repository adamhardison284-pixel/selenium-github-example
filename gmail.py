import tempfile
import shutil
import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import requests
from supabase import create_client, Client
from faster_whisper import WhisperModel

"""
python gmail.py
"""

ip = requests.get("https://api.ipify.org?format=json").json()["ip"]

url_ = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"

profile_dir = tempfile.mkdtemp()
chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
chromedriver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

options = uc.ChromeOptions()
options.binary_location = chrome_bin
options.add_argument("--headless")
options.add_argument(f"--user-data-dir={profile_dir}")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail.com%26oq%3Dgmail%26gs_lcrp%3DEgZjaHJvbWUqBwgBEAAYjwIyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIGCAMQRRg9MgYIBBBFGD3SAQgzMTAxajBqNKgCALACAQ%26sourceid%3Dchrome%26ie%3DUTF-8&dsh=S-1894901072%3A1764852364751767&ec=futura_srp_og_si_72236_p&hl=fr&ifkv=ARESoU16T_GnNuZ0_jDfKA7W7GSa0ZNwFJ_TNwIRGIXc3uKOwUcwczEv6GWc0OlMyQsuh5bnlkRM&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
driver = uc.Chrome(service=Service(chromedriver_path), options=options)
driver.maximize_window()
driver.get(url)
actions = ActionChains(driver)
print(driver.title)


src = f"""
function setNativeValue(element, value) {{
  const lastValue = element.value;
  element.value = value;

  const event = new Event("input", {{ bubbles: true }});

  const tracker = element._valueTracker;
  if (tracker) tracker.setValue(lastValue);

  element.dispatchEvent(event);
}};
let ss = document.querySelector('[id="identifierId"]')
setNativeValue(ss, 'azamkhandcc110@gmail.com')
document.querySelector('\div[id="identifierNext"]').querySelector('button').click()
"""
driver.execute_script(src)
time.sleep(5)
print('check captcha')
print(driver.title)
driver.save_screenshot("screenshot_1.png")
driver.quit()
