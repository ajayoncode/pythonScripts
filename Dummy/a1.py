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
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

def display_notification(message):
    # Escape the double quotes in the message for the AppleScript string
    escaped_message = message.replace('"', '\\"')
    applescript = f'display notification "{escaped_message}"'
    subprocess.run(['osascript', '-e', applescript], capture_output=True)
    time.sleep(10)

def test_google_search():
    try:
        # Open the website
        driver.get('https://ajey.vercel.app')

        username = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > input:nth-child(2)')
        username.send_keys('rnd')
        password = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > input:nth-child(3)')
        password.send_keys('1.1.1')
        
        getInButton = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div.css-175oi2r.r-1i6wzkk.r-lrvibr.r-1loqt21.r-1otgn73')
        getInButton.click()

        time.sleep(5)
        search = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div.css-175oi2r.r-1i6wzkk.r-lrvibr.r-1loqt21.r-1otgn73 > div.css-1rynq56')
        search.click()

        searchBox = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > textarea')
        searchCLI = input('Search For : ')
        print('\n Searching..', searchCLI)
        searchBox.send_keys(searchCLI)
        # selectBook = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div > div')
        # selectBook.click()

        con = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.css-175oi2r.r-1i6wzkk.r-lrvibr.r-1loqt21.r-1otgn73 > div > div:nth-child(2) > div > textarea')
        # driver.save_screenshot("screenshot.png")
        showThis = con.text
        print('>>> ',showThis)
        pyperclip.copy(showThis)
        display_notification("Item copied: " + showThis)

        time.sleep(10)
        # Verify the expected content or title on the page to confirm success
        print('Test passed!')
        time.sleep(50)

    except AssertionError as e:
        print('Test failed:', str(e))
    finally:
        # Close the browser
        driver.quit()

def create_reminder(title, notes, due_date):
    command = [
        '/System/Applications/reminders',  # Replace with the actual path to the reminders command
        'add',
        '--title', title,
        '--notes', notes,
        '--due', due_date
    ]
    subprocess.run(command)

reminder_title = "A Project"
reminder_notes = "Complete the final report and submit it."
reminder_due_date = "2023-08-10 09:14:50"  # Corrected ISO 8601 date and time format



if __name__ == "__main__":
    test_google_search()
    # create_reminder(reminder_title, reminder_notes, reminder_due_date)
