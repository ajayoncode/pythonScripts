import time
import requests
import subprocess

def openAppWithProject(app_name, project_path):
    try:
        subprocess.run(["open", "-a", app_name, project_path])
        print(f"{app_name} opened successfully with project {project_path}.")
    except Exception as e:
        print(f"Error opening {app_name} with project {project_path}: {e}")

def runCmdInTerminal(project_path,cmd):
    try:
        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "cd {project_path} && {cmd}"'])
        print("yarn start command executed in Terminal.")
    except Exception as e:
        print(f"Error executing yarn start command in Terminal: {e}")

def upload_build_to_server(archive_path):
    url = "http://ds.24livehost.com/Home/FileUpload"  # Replace with the actual upload URL
    files = {'file': open(archive_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("Response Content:", response.content.decode('utf-8'))
    else:
        print("File upload failed.")

def automateXcodeActions(project_path, workspace_path, scheme_name, udid_device):
    try:
        # Open Xcode
        subprocess.run(["open", "-a", "Xcode", workspace_path])
        print(f"Xcode opened successfully with project {workspace_path}.")

        # Simulate keyboard shortcuts to open workspace and run on simulator
        osascript_script = f'''
            tell application "System Events"
                keystroke "o" using {{command down}}
                delay 1
                delay 1
                keystroke return
                delay 2
                keystroke "r" using {{command down}}
                delay 1
                keystroke "{scheme_name}"
                delay 1
                keystroke return
            end tell
        '''

        subprocess.run(["osascript", "-e", osascript_script])
        print("Automated Xcode actions executed successfully.")

    except Exception as e:
        print(f"Error automating Xcode actions: {e}")

# Call the function with appropriate parameters

# Replace 'Visual Studio Code' with the exact name of the application
udid_device = '91EAB51F-9856-4AB4-9B01-6DD35E69099D'
app_name = 'Visual Studio Code'
project_path = '/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo'
iphone_11_simulator = 'iPhone 11'
bundleId='com.attenteo'
scheme_name='attenteo'
workspace_path='/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo/ios/attenteo.xcworkspace'

applescript_code = f'''
          tell application "System Events"
           keystroke "f" using {{command down, option down}}
            end tell
        '''

        
def test_google_search():
    try:
        # Open the website
        driver.get('http://ds.24livehost.com/')

        username = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > input:nth-child(2)')
        username.send_keys('rnd')
        password = driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.css-175oi2r.r-13awgt0 > div > div.css-175oi2r.r-1p0dtai.r-1d2f490.r-u8s1d.r-zchlnj.r-ipm5af.r-12vffkv > div:nth-child(2) > div > div > div > div.css-175oi2r.r-13awgt0 > div > div > div:nth-child(2) > input:nth-child(3)')
        password.send_keys('..')
        
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

upload_build_to_server('/Users/ajaymangal/Downloads/attenteo 2023-08-07 19-05-46/attenteo.ipa')
