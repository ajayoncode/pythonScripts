from setuptools import setup

APP = ['mac1.py']  # Replace 'your_script.py' with your actual script filename
DATA_FILES = []  # Add any additional data files or resources your script needs
OPTIONS = {
    'argv_emulation': True,  # Use this option if your script uses command-line arguments
    'packages': ['subprocess'],  # List any additional packages your script imports
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
