import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pickle5 as pickle

_URL = 'https://vendorcentral.amazon.co.uk/home/vc'
_CookiePath = './cookienow'

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    print('>>> 3')
    try:
        with open(path, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            print('>>> 4',cookies)

            for cookie in cookies:
                    if 'expiry' in cookie:
                        del cookie['expiry']
                    driver.add_cookie(cookie)
                
            time.sleep(6)    
    
    except FileNotFoundError:
        print(f'Cookie file "{path}" not found.')
    except Exception as e:
        print(f'Error loading cookies: {str(e)}')

def test_google_search():
    driver = None  # Initialize driver to None
    try:
        # Initialize the WebDriver
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://vendorcentral.amazon.co.uk')
        driver.delete_all_cookies()
        driver.get(_URL)
        
        load_cookie(driver,_CookiePath)

        driver.refresh()
        driver.get(_URL)
        print('@@C1')
        
        
        print('Loaded cookie1')

        # Perform actions
        try:
            emailInput = driver.find_element(By.ID, 'ap_email')
            emailInput.send_keys('Himalaya@VisualCOGS.com')

            passwordInput = driver.find_element(By.ID, 'ap_password')
            passwordInput.send_keys('himalya@vc@12')
            
            signInSubmit = driver.find_element(By.ID, 'signInSubmit')
            signInSubmit.click()
        except:
            print('@@ Failed in Normal login')
        
        
        time.sleep(50)
        print('saving cookies!')
        selectAccountOption = driver.find_element(By.XPATH,'//*[@id="sc-content-container"]/div/div[1]/div[2]/div/button[1]')
        selectAccountOption.click()
        selectAccount = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div[3]/button')
        selectAccount.click()

        
        time.sleep(10)
        save_cookie(driver,_CookiePath)
        
        print('Test passed!')
    except Exception as e:
        print('Test failed:', str(e))
    finally:
        # Close the browser
        if driver:
            driver.quit()


if __name__ == "__main__":
    test_google_search()
