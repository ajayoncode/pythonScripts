import time
import requests
import subprocess
import pyperclip

folderPath = '/Users/ajaymangal/Downloads/attenteo 2023-08-07 19-05-46/attenteo.ipa'

def upload_build_to_server(archive_path):
    path = input('Paste path here : ')
    print('Uploading form : ',path)
    url = "http://ds.24livehost.com/Home/FileUpload"  # Replace with the actual upload URL
    files = {'file': open(path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        publicLink = response.content.decode('utf-8')
        print("Response Content:", publicLink)
        pyperclip.copy(publicLink)
        display_notification("Item copied: " + publicLink)
    else:
        print("File upload failed.")

def display_notification(message):
    # Escape the double quotes in the message for the AppleScript string
    escaped_message = message.replace('"', '\\"')
    applescript = f'display notification "{escaped_message}" with title "Copied!"'
    subprocess.run(['osascript', '-e', applescript], capture_output=True)
    time.sleep(10)

# def takeInputs():
    # path = input('Enter path here : ')
    

# takeInputs()
upload_build_to_server(folderPath)
