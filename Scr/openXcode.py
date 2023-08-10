# Debug in Xcode
# Ask to change simulator and debug xcode and open visual studio 
# First waiting for 10 sec for input otherwise open default
# Now its ask user want to arch or debug in xCode, will arch in terminal as given path
 

import time
import subprocess
import os
import sys
import select

def runAppleScript(applescript_code):
    try:
        subprocess.run(["osascript", "-e", applescript_code])
        print("AppleScript executed successfully.")

    except Exception as e:
        print(f"Error executing AppleScript: {e}")

def pressKey(key_code):
    try:
        applescript_code = f'''
            tell application "System Events"
                key code {key_code}
            end tell
        '''
        subprocess.run(["osascript", "-e", applescript_code])
        print("Key pressed successfully.")

    except Exception as e:
        print(f"Error pressing key: {e}")

def automateXcodeActions(project_path, workspace_path, scheme_name, udid_device):
    try:
        # Open Xcode
        subprocess.run(["open", "-a", "Xcode", workspace_path])
        print(f"Xcode opened successfully with project {workspace_path}.")


        print(f"Enter simulator name you want to run like [iPhone 12, iPhone 11]")
        i, o, e = select.select([sys.stdin], [], [], 10)
        
        udid_device1 = udid_device
        if i:
            udid_device1 = sys.stdin.readline().strip()
            print(f"User input received: {udid_device1}")
        else:
            print("No user input received. Continuing with default behavior.")
            
        
        change_simulator(udid_device1)

        # Simulate keyboard shortcuts to open workspace and run on simulator
        time.sleep(2)
        osascript_script = f'''
            tell application "System Events"
                delay 2
                keystroke "r" using {{command down}}
                delay 1
            end tell
        '''

        subprocess.run(["osascript", "-e", osascript_script])
        print("Automated Xcode actions executed successfully.")

    except Exception as e:
        print(f"Error automating Xcode actions: {e}")

def createArchieve(project_path,workspace_path,scheme_name):
    change_simulator('Any iOS Device (arm64)')
    print('Creating archive...')
    # Archive the project using xcodebuild
    try:
        archive_command = ["xcodebuild", "-workspace", workspace_path, "-scheme", scheme_name, "archive", "-archivePath", "/Users/ajaymangal/Downloads"]
        subprocess.run(archive_command)
    except Exception as e:
        print(f"Error automating Xcode Archive: {e}")

def change_simulator(device_name):
    applescript = f'''
        tell application "Xcode"
            activate
            tell application "System Events"
                tell process "Xcode"
                    click menu item "{device_name}" of menu 1 of menu item "Destination" of menu 1 of menu bar item "Product" of menu bar 1
                end tell
            end tell
        end tell
    '''

    subprocess.run(['osascript', '-e', applescript])


app_name = 'Visual Studio Code'
project_path = '/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo'
iphone_11_simulator = 'iPhone 11'
bundleId='com.attenteo'
scheme_name='attenteo'
workspace_path='/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo/ios/attenteo.xcworkspace'
forArchieve= 'Any iOS Device (arm64)'
applescript_code = f'''
          tell application "System Events"
           keystroke "f" using {{command down, option down}}
            end tell
        '''





mainInput = input('Enter "arch" for creating Archive, or anything else to debug in Xcode: ')

if mainInput == 'arch':
    createArchieve(project_path, workspace_path, scheme_name)
else: 
    automateXcodeActions(project_path, workspace_path, scheme_name, iphone_11_simulator)

print('Success!!')
time.sleep(7)
# openAppWithProject(app_name, project_path)
time.sleep(3)
# runAppleScript(applescript_code)
# pressKey('122')
