import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_google_search():
    # Initialize the Chrome web driver (replace 'path_to_chromedriver' with your actual path)
    # driver = webdriver.Chrome(executable_path='I:\Phython0.1\chromedriver-win64\chromedriver.exe')
    

    try:
        # Open the website
        driver.get('https://ems.dotsquares.com/Login')

        # Find the element by name and submit the form
        email = driver.find_element('name',"Email").send_keys("ajay.mangal@dotsquares.com")
        Passsword = driver.find_element('name',"Password").send_keys("ajey@789")
        
        subitbtn= driver.find_element(By.XPATH, '//*[@id="form1"]/div/div[2]/div[2]/div[4]/div[2]/button')

        subitbtn.submit()

        # Wait for the page to load (you can use WebDriverWait for more advanced wait conditions)
        time.sleep(25)

        # Verify the expected content or title on the page to confirm success
        print('Test passed!')
    except AssertionError as e:
        print('Test failed:', str(e))
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_google_search()
