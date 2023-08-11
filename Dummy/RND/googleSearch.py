import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import pyperclip
import subprocess
from datetime import datetime

chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)


def test_google_search():
    try:
        # Open the website
        driver.get('https://www.google.com/')
        test = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
        test.send_keys('ajay')
        time.sleep(15)




    except AssertionError as e:
        print('Test failed:', str(e))
    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    test_google_search()
    # create_reminder(reminder_title, reminder_notes, reminder_due_date)
