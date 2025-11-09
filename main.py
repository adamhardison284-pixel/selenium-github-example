from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def main():
    # Configure Chrome options for headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Create the driver
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://sprintmail.ru/"
        driver.get(url)

        print("Page title:", driver.title)

        # Save a screenshot to verify it worked
        driver.save_screenshot("screenshot.png")
        print("Screenshot saved as screenshot.png")

        # Example: find an element
        heading = driver.find_element(By.TAG_NAME, "h1").text
        print("Heading text:", heading)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
