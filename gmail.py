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
thus = True
while thus:
    captcha = driver.execute_script("return document.querySelectorAll('[title=\"reCAPTCHA\"]')")
    print('captcha: ', len(captcha))
    if len(captcha) > 0:
        driver.switch_to.frame(captcha[0])
        thus = False
        anch = driver.find_element(By.ID, "recaptcha-anchor")
        actions.move_to_element(anch).click(anch).perform()
        time.sleep(3)
        thus_2 = True
        incc = 0
        while thus_2:
                anch = driver.find_element(By.ID, "recaptcha-anchor")
                if anch.get_attribute("aria-checked") == "true":
                    thus_2 = False
                    driver.switch_to.default_content()
                    
                    thus_1 = True
                    inc = 0
                    while thus_1:
                        if inc < 5:
                            try:
                                #btnns = driver.execute_script("return document.querySelectorAll('.cl-v3-btn-base.cl-v3-btn-base--main.cl-v3-btn-base--lg')")
                                btnns = driver.find_elements(By.TAG_NAME, "button")
                                for bt in btnns:
                                    if bt.get_attribute("class") == "cl-v3-btn-base cl-v3-btn-base--main cl-v3-btn-base--lg":
                                        actions.move_to_element(bt).click(bt).perform()
                                        break
                                time.sleep(1)
                                inc = inc + 1
                            except:
                                inc = inc + 1
                                time.sleep(1)
                                print('errrr')
                        else:
                            thus_1 = False
                else:
                    print('audio captcha')
                    thus_2 = False
                    driver.switch_to.default_content()
                    captchas = driver.execute_script("return document.querySelectorAll('[title=\"recaptcha challenge expires in two minutes\"]')")
                    print('captchas: ', len(captchas))
                    driver.switch_to.frame(captchas[0])
                    bttns = driver.find_elements(By.TAG_NAME, "button")
                    
                    for bttn in bttns:
                        try:
                            if bttn.get_attribute("class") == "rc-button goog-inline-block rc-button-audio":
                                
                                driver.execute_script("document.getElementsByClassName('rc-button goog-inline-block rc-button-audio')[0].click()")
                        except:
                            pass
                        
                    bttns = driver.find_elements(By.TAG_NAME, "button")
                    for bttn in bttns:
                        try:
                            if bttn.get_attribute("class") == "rc-button-default goog-inline-block":
                                
                                driver.execute_script("document.getElementsByClassName('rc-button-default goog-inline-block')[0].click()")
                        except:
                            pass
                    
                    auds = driver.find_elements(By.TAG_NAME, "a")
                    for aud in auds:
                        if aud.get_attribute("class") == "rc-audiochallenge-tdownload-link":
                            aud_link = str(aud.get_attribute("href"))
                            print('aud_link: ', aud_link)
                            response = requests.get(aud_link)

                            with open("audio.mp3", "wb") as f:
                                f.write(response.content)
                                                                
                            model = WhisperModel("small")

                            segments, info = model.transcribe("audio.mp3")

                            text = ""
                            for seg in segments:
                                text += seg.text + " "

                            bttns = driver.find_elements(By.TAG_NAME, "input")
                            for bttn in bttns:
                                try:
                                    if bttn.get_attribute("id") == "audio-response":
                                        bttn.send_keys(text, Keys.ENTER)
                                        time.sleep(2)
                                except:
                                    pass
                            break
                    
                    trthu = True
                    while trthu:
                        btntns = driver.find_elements(By.TAG_NAME, "div")
                        for btntn in btntns:
                            try:
                                if btntn.get_attribute("class") == "rc-audiochallenge-error-message":
                                    text = driver.execute_script("return arguments[0].innerText;", btntn)
                                    if "Multiple correct solutions" in text:
                                        btntnss = driver.execute_script('return document.getElementsByClassName("rc-button goog-inline-block rc-button-reload")')
                                        for btntnss_ in btntnss:
                                            try:
                                                if btntnss_.get_attribute("class") == "rc-button goog-inline-block rc-button-reload":
                                                    #actions.move_to_element(btntnss_).click(btntnss_).perform()
                                                    driver.execute_script('return document.getElementsByClassName("rc-button goog-inline-block rc-button-reload")[0].click()')
                                                    time.sleep(2)
                                                    bttns = driver.find_elements(By.TAG_NAME, "button")
                                                    for bttn in bttns:
                                                        try:
                                                            if bttn.get_attribute("class") == "rc-button-default goog-inline-block":
                                                                
                                                                driver.execute_script("document.getElementsByClassName('rc-button-default goog-inline-block')[0].click()")
                                                        except:
                                                            pass
                                                    
                                                    auds = driver.find_elements(By.TAG_NAME, "a")
                                                    for aud in auds:
                                                        if aud.get_attribute("class") == "rc-audiochallenge-tdownload-link":
                                                            aud_link = str(aud.get_attribute("href"))
                                                            print('aud_link: ', aud_link)
                                                            response = requests.get(aud_link)

                                                            with open("audio.mp3", "wb") as f:
                                                                f.write(response.content)
                                                                
                                                            model = WhisperModel("small")

                                                            segments, info = model.transcribe("audio.mp3")

                                                            text = ""
                                                            for seg in segments:
                                                                text += seg.text + " "
                                                                
                                                            """
                                                            # Step 2: Load Whisper model
                                                            model = whisper.load_model("base")

                                                            # Step 3: Transcribe the downloaded file
                                                            result = model.transcribe("temp.mp3")
                                                            """
                                                            
                                                            bttns = driver.find_elements(By.TAG_NAME, "input")
                                                            for bttn in bttns:
                                                                try:
                                                                    if bttn.get_attribute("id") == "audio-response":
                                                                        bttn.send_keys(text, Keys.ENTER)
                                                                        time.sleep(2)
                                                                except:
                                                                    pass
                                                            break
                                                    break
                                            except:
                                                pass
                                    break
                            except:
                                pass
                        trthu = False
    else:
        thus = False
src = f"""
function setNativeValue(element, value) {{
  const lastValue = element.value;
  element.value = value;

  const event = new Event("input", {{ bubbles: true }});

  const tracker = element._valueTracker;
  if (tracker) tracker.setValue(lastValue);

  element.dispatchEvent(event);
}};
let sss = document.querySelector('[name="Passwd"]')
setNativeValue(sss, 'ArbiNaji1987$')
document.querySelector('\div[id="passwordNext"]').querySelector('button').click()
"""

print('check password')
th_name = True
while th_name:
    mames = driver.execute_script("return document.querySelectorAll('[name=\"Passwd\"]')")
    if len(mames) > 0:
        th_name = False
driver.execute_script(src)
time.sleep(10)

print('check email recovery...')
mames_2 = driver.execute_script("return document.querySelectorAll('div[class=\"VV3oRb YZVTmd SmR8\"]')")
if len(mames_2) > 0:
    src = """
    const elementsWithText = Array.from(document.querySelectorAll('div[class="VV3oRb YZVTmd SmR8"]')).filter(element => {
      return element.innerText.includes('Confirm');
    });
    elementsWithText[0].click()
    """
    driver.execute_script(src)
    time.sleep(10)

    src = f"""

    function setNativeValue(element, value) {{
      const lastValue = element.value;
      element.value = value;

      const event = new Event("input", {{ bubbles: true }});

      const tracker = element._valueTracker;
      if (tracker) tracker.setValue(lastValue);

      element.dispatchEvent(event);
    }};
    let ss = document.querySelector('[id="knowledge-preregistered-email-response"]')
    setNativeValue(ss, 'arbi.naji@gmail.com')
    document.querySelector('button[jscontroller="soHxf"').click()

    """
    driver.execute_script(src)
    time.sleep(10)
  
url = "https://mail.google.com/mail/u/0/#inbox/"
driver.get(url)

src = f"""
    const policy = trustedTypes.createPolicy('default', {{
      createHTML: (input) => input, // sanitize properly in production
    }});
"""
#driver.execute_script(src)
src_1 = f"""
    const policy = trustedTypes.createPolicy('default', {{
      createHTML: (input) => input, // sanitize properly in production
    }});
    
    const element = document.querySelector('.Am.aiL.Al.editable');
    msg = `
        <p>Hallo,</p>`
    msg= msg.replaceAll('[em]', 'adamoyler2705cc@web.de')
    msg= msg.replaceAll('[of_id]', '8')
    element.innerHTML = policy.createHTML(msg);
  """
src_2 = """
    const ell = Array.from(document.querySelectorAll('div[role="button"]'))
    .find(e => e.textContent.includes("Envoyer") || e.textContent.includes("Send"));

    if (ell) ell.click();
"""

th_compose = True
while th_compose:
    composes = driver.execute_script("return document.querySelectorAll('[class=\"T-I T-I-KE L3\"]')")
    if len(composes) > 0:
        
        time.sleep(5)
        driver.execute_script("document.querySelectorAll('[class=\"T-I T-I-KE L3\"]')[0].click()")
        th_compose = False
        
th_recepient = True
while th_recepient:
    recepients = driver.execute_script("return document.querySelectorAll('[class=\"agP aFw\"]')")
    if len(recepients) > 0:
        time.sleep(1)
        em = "arbi.naji@gmail.com"
        driver.execute_script(f"document.querySelectorAll('[class=\"agP aFw\"]')[0].value = \"{em}\"")
        th_recepient = False
        
th_recepient = True
while th_recepient:
    recepients = driver.execute_script("return document.querySelectorAll('[placeholder=\"Subject\"], [placeholder=\"Objet\"]')")
    if len(recepients) > 0:
        time.sleep(1)
        subject = "🎁 Gratis-Produkte sichern – Uhren, Deko, Schuhe & mehr!"
        driver.execute_script(f"document.querySelectorAll('[placeholder=\"Subject\"], [placeholder=\"Objet\"]')[0].value = \"{subject}\"")
        th_recepient = False
        time.sleep(2)
        driver.execute_script(src_1)
        time.sleep(5)
        driver.execute_script(src_2)
        time.sleep(2)
        
        
time.sleep(1)
