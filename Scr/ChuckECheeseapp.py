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

def runCmdInTerminal(project_path,cmd):
    try:
        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "cd {project_path} && {cmd}"'])
        print("yarn start command executed in Terminal.")
    except Exception as e:
        print(f"Error executing yarn start command in Terminal: {e}")


app_name = 'Visual Studio Code'
project_path = '/Users/punchh_vijaym/WorkingProjects_2/chuck-e-cheese-app-app/ChuckECheeseapp'
iphone_11_simulator = 'iPhone 14'
bundleId='com.chuckecheese.app'
scheme_name='ChuckECheeseapp'
workspace_path='/Users/punchh_vijaym/WorkingProjects_2/chuck-e-cheese-app-app/ChuckECheeseapp/ios/ChuckECheeseapp.xcworkspace'
applescript_code = f'''
          tell application "System Events"
           keystroke "f" using {{command down, option down}}
            end tell
        '''


automateXcodeActions(project_path, workspace_path, scheme_name, iphone_11_simulator)

print('Success!!')
time.sleep(3)
runCmdInTerminal(project_path,'npm start -- --reset-cache')
time.sleep(3)

# pressKey('122')
