from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def main():
    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

    options = Options()
    options.binary_location = chrome_bin
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    url = "https://sprintmail.ru/"
    driver.get(url)
    print("Title:", driver.title)
    driver.save_screenshot("screenshot.png")
    driver.quit()

if __name__ == "__main__":
    main()
