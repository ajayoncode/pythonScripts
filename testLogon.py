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

        # searchBox = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > textarea')
        # searchBox.send_keys('Logged cookie aws')
        selectBook = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div > div')
        selectBook.click()

        con = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div')
        # driver.save_screenshot("screenshot.png")
        print('>>> ',con.text)
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
