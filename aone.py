import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_google_search():
    # Initialize the Chrome web driver (replace 'path_to_chromedriver' with your actual path)
    # driver = webdriver.Chrome(executable_path='I:\Phython0.1\chromedriver-win64\chromedriver.exe')
    

    try:
        # Open the website
        driver.get('https://admin-demo.nopcommerce.com/')

        # Find the element by name and submit the form
        remember_me_checkbox = driver.find_element("name","RememberMe")
        remember_me_checkbox.submit()

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
