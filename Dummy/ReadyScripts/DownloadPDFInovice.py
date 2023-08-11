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
        driver.get('https://admin-demo.nopcommerce.com/')

        # Find the element by name and submit the form
        remember_me_checkbox = driver.find_element("name","RememberMe")
        remember_me_checkbox.submit()

        # Wait for the page to load (you can use WebDriverWait for more advanced wait conditions)
        time.sleep(2)
        # input_element = driver.find_element(By.CLASS_NAME, 'form-control')
        # Input a value into the element
        # input_element.send_keys('Money')

        onSalesButton= driver.find_element(By.XPATH, '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]')
        # time.sleep(2)
               
        onSalesButton.click()
        onOrderButton= driver.find_element(By.XPATH, '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[1]')
        onOrderButton.click()
        mastercheckbox= driver.find_element(By.CLASS_NAME, 'mastercheckbox')
        mastercheckbox.click()
        printInvoiceOption= driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/form[1]/div/div/div[2]/button[2]')
        printInvoiceOption.click()
        printSelectedPDF= driver.find_element(By.ID, 'pdf-invoice-selected')
        printSelectedPDF.click()
        
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
