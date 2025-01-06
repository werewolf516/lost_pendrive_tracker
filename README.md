Lost Pendrive Tracking and USB Access System
This project includes two scripts designed for tracking geolocation information and controlling access to a USB device. It also enables the transmission of geolocation data to an owner's server.

Features
Tracks geolocation using IP.
Prompts for password-protected access to a USB device.
Sends geolocation data to an owner's server.
File Overview
owner_server.py

A Flask-based server script to receive and log geolocation data sent from the USB tracking script.
track_pendrive.py

A Python script that:
Displays owner information.
Requires a password for USB access.
Fetches geolocation data and sends it to the server.
Prerequisites
For Running the Scripts
Python Version: Python 3.6+
Required Python Libraries:
Flask (for owner_server.py)
requests
tkinter
Installation of Dependencies
Run the following command to install the required libraries:

bash
Copy code
pip install flask requests
Setting Up the Project
Step 1: Clone the Repository
Upload your files to a GitHub repository and clone it using:

bash
Copy code
git clone https://github.com/<your_username>/<repository_name>.git
Step 2: Configure track_pendrive.py
Update the following line in track_pendrive.py with your server's IP address:

python
Copy code
SERVER_URL = "http://<your_server_ip>:5000/receive-data"
Running the Project
Step 1: Start the Server
Navigate to the directory containing owner_server.py.
Run the following command:
bash
Copy code
python owner_server.py
This will start the Flask server at http://0.0.0.0:5000.
Step 2: Run the USB Tracker Script
Navigate to the directory containing track_pendrive.py.

Execute the script:

bash
Copy code
python track_pendrive.py
The script will:

Show owner information and prompt for a password.
Fetch geolocation data.
Send the data to the server at the specified SERVER_URL.
Automating the Execution
To automatically execute track_pendrive.py upon USB insertion:

Windows:

Create a .bat file with the following content:
bat
Copy code
python path\\to\\track_pendrive.py
Place the .bat file in the USB drive and configure it to auto-run using Windows AutoPlay settings.
Linux:

Add an auto-run script to /etc/udev/rules.d/.
Example Rule:
bash
Copy code
ACTION=="add", KERNEL=="sdb1", RUN+="/usr/bin/python3 /path/to/track_pendrive.py"
MacOS:

Use launchd to create a plist file that executes the script when the USB is mounted.
Notes
Ensure the server is running before executing track_pendrive.py.
Update the OWNER_NAME, OWNER_EMAIL, CONTACT_NUMBER, and ACCESS_PASSWORD in track_pendrive.py as per your requirements.
License
This project is licensed under the MIT License.
