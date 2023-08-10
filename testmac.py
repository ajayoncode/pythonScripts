import subprocess

PROJECT_PATH = "/Users/ajaymangal/Master/RN_Project2.0/RN_Attenteo/ios/attenteo.xcworkspace"
BUNDLE_IDENTIFIER = "com.attenteo"
SIMULATOR_UDID = "91EAB51F-9856-4AB4-9B01-6DD35E69099D"  # Replace with the actual UDID
app_name = 'Visual Studio Code'
YourScheme= "attenteo"

def build_and_run_debug():
    try:
        # Build with Debugging Symbols
        build_command = [
            "xcodebuild",
            "-workspace",  # Use -workspace instead of -project
            PROJECT_PATH,
            "-scheme",
            YourScheme,  # Replace with your scheme name
            "-configuration",
            "Debug",
            "build"
        ]
        subprocess.run(build_command, check=True)
        print("Xcode project built with debugging symbols.")

        # Install and launch on simulator
        install_command = [
            "xcrun",
            "simctl",
            "install",
            SIMULATOR_UDID,
            PROJECT_PATH
        ]
        subprocess.run(install_command, check=True)

        launch_command = [
            "xcrun",
            "simctl",
            "launch",
            SIMULATOR_UDID,
            BUNDLE_IDENTIFIER
        ]
        subprocess.run(launch_command, check=True)
        print("Xcode project launched on the simulator in debug mode.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Failed to build or run Xcode project.")

if __name__ == "__main__":
    build_and_run_debug()
