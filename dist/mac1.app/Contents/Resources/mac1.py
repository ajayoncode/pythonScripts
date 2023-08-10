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

def openProjectInXcode(project_path, workspace_path, udidDevice):
    try:
        # Open Xcode with the specified project
        subprocess.run(["open", "-a", "Xcode", project_path])
        print(f"Xcode opened successfully with project {project_path}.")

        # Build and run the project on a simulator using xcodebuild
        build_command = [
            "xcodebuild",
            "-workspace", workspace_path,  # Path to your Xcode workspace
            "-scheme", "attenteo",       # Replace with the scheme name of your project
            "-destination", f"id={udidDevice}",  # UDID of the simulator device
            "clean", "build", "test"      # Build, test, and run the project
        ]
        subprocess.run(build_command)
        print(f"Project built and run on simulator {udidDevice}.")

    except Exception as e:
        print(f"Error opening Xcode with project {project_path}: {e}")

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
                delay 1
                keystroke "{udid_device}"
                delay 1
                keystroke return
            end tell
        '''

        subprocess.run(["osascript", "-e", osascript_script])
        print("Automated Xcode actions executed successfully.")

    except Exception as e:
        print(f"Error automating Xcode actions: {e}")


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

# Replace 'Visual Studio Code' with the exact name of the application
udid_device = '91EAB51F-9856-4AB4-9B01-6DD35E69099D'
app_name = 'Visual Studio Code'
project_path = '/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo'
iphone_11_simulator = 'iPhone 11'
bundleId='com.attenteo'
scheme_name='attenteo'
workspace_path='/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo/ios/attenteo.xcworkspace'

# runCmdInTerminal(project_path,'xcrun simctl list devices')
# Open the project in Xcode
# openProjectInXcode(project_path,'/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo/ios/attenteo.xcworkspace',udidDevice)
automateXcodeActions(project_path, workspace_path, scheme_name, udid_device)
delay(10)
openAppWithProject(app_name, project_path)
# pressKey('122')
