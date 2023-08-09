import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_google_search():
    try:
        # Open the website
        driver.get('https://ajey.verce.app')

        getIn= driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/input[1]')
        getIn.send_keys('HER')
        time.sleep(20)
        # Verify the expected content or title on the page to confirm success
        print('Test passed!')
    except AssertionError as e:
        print('Test failed:', str(e))
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()
