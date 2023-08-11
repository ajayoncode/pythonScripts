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
        subprocess.run(["open", "-a", "Xcode_14.2.app", workspace_path])
        print(f"Xcode opened successfully with project {workspace_path}.")
        print("Automated Xcode actions executed successfully.")
    except Exception as e:
        print(f"Error automating Xcode actions: {e}")


def runCmdInTerminal(project_path, cmd):
    try:
        subprocess.run(f'cd {project_path} && {cmd}', shell=True, executable='/bin/bash')
        print("yarn start command executed.")
    except Exception as e:
        print(f"Error executing yarn start command: {e}")


app_name = 'Visual Studio Code'
project_path = '/Users/punchh_vijaym/WorkingProjects_2/chuck-e-cheese-app-app/ChuckECheeseapp'
iphone_11_simulator = 'iPhone 14'
bundleId='com.chuckecheese.app'
scheme_name='ChuckECheeseapp'
workspace_path='/Users/punchh_vijaym/WorkingProjects_2/chuck-e-cheese-app-app/ChuckECheeseapp/ios/ChuckECheeseapp.xcworkspace'

automateXcodeActions(project_path, workspace_path, scheme_name, iphone_11_simulator)

print('Success!!')
runCmdInTerminal(project_path,'npm start')
sys.exit()
