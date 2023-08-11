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
from functools import partial
from mac_notifications import client
import schedule

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

def runAppleScript(applescript_code):
    try:
        subprocess.run(["osascript", "-e", applescript_code])
        print("AppleScript executed successfully.")

    except Exception as e:
        print(f"Error executing AppleScript: {e}")


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

        TIME = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.css-175oi2r.r-1i6wzkk.r-lrvibr.r-1loqt21.r-1otgn73 > div > div:nth-child(2) > div > input').text
        CONTENT = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.css-175oi2r.r-1i6wzkk.r-lrvibr.r-1loqt21.r-1otgn73 > div > div:nth-child(1) > div > textarea').text
        # LAST_UPDATED = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div').text
        print('Title : ',TIME)
        print('Content : ',CONTENT)
        # print('Updated On ',LAST_UPDATED)

        # pyperclip.copy(CONTENT)
        # display_notification("Item copied: " + showThis)
        print('Test 1!')
        # create_notification(CONTENT,TITLE)
        main('Notification here for you',CONTENT)
        time.sleep(1)
        print('DONE')
        quit()
        driver.quit()
    except AssertionError as e:
        print('Test failed:', str(e))
    finally:
        # Close the browser
      

def create_notification(CONTENT,TITLE):
    client.create_notification(
        title=CONTENT,
        subtitle=TITLE,
        # icon="/Users/ajaymangal/Master/_Ajex/DEV/main/Python0.1/P2/Scr/WebTest/completeActive.png",
        action_button_str="Okay",
        # action_callback=partial(join_zoom_meeting, conf_number=zoom_conf_number)
    )

def send_notification(message):
    applescript = f'display notification "{message}" with title "Ajay"'
    subprocess.run(['osascript', '-e', applescript])

def main(msg,time):
    print('>>> ',time)
    notification_time = '19:06:55'  # Set the desired time
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == notification_time:
            send_notification(msg)
            break
        time.sleep(1)  # Wait for 1 second before checking again


if __name__ == "__main__":
    test_google_search()
    # create_reminder(reminder_title, reminder_notes, reminder_due_date)
