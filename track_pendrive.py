import os
import requests
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

# Owner information
OWNER_NAME = "John "
OWNER_EMAIL = "abc@example.com"
CONTACT_NUMBER = "+1-123-456-7890"
ACCESS_PASSWORD = "1234"
SERVER_URL = "http://"owners ip":5000/receive-data"  # Replace with owner's server IP

# Function to get geolocation based on IP
def get_geolocation():
    try:
        response = requests.get("http://ip-api.com/json/")
        if response.status_code == 200:
            data = response.json()
            location_info = {
                "ip": data.get("query", "N/A"),
                "country": data.get("country", "N/A"),
                "region": data.get("regionName", "N/A"),
                "city": data.get("city", "N/A"),
                "zip": data.get("zip", "N/A"),
                "latitude": data.get("lat", "N/A"),
                "longitude": data.get("lon", "N/A"),
                "timezone": data.get("timezone", "N/A"),
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            return location_info
        else:
            return {"error": "Failed to fetch geolocation"}
    except Exception as e:
        return {"error": str(e)}

# Function to send data to the owner's server
def send_to_owner_server(location_info):
    try:
        response = requests.post(SERVER_URL, json=location_info)
        if response.status_code == 200:
            print("Data successfully sent to the owner's server.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

# Function to display owner information and password dialog
def show_owner_info():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Display owner information
    messagebox.showinfo(
        "Pendrive Owner Information",
        f"Owner Name: {OWNER_NAME}\nEmail: {OWNER_EMAIL}\nContact: {CONTACT_NUMBER}\n\n"
        "Please enter the password to access the USB drive."
    )

    # Ask for a password
    entered_password = simpledialog.askstring(
        "Access Restricted",
        "Enter the password to access the USB drive:",
        show="*"
    )

    if entered_password == ACCESS_PASSWORD:
        messagebox.showinfo("Access Granted", "Welcome! You can now access the USB contents.")
        return True
    else:
        messagebox.showerror("Access Denied", "Incorrect password. USB access is restricted.")
        return False

# Main execution
if __name__ == "__main__":
    print("Running geolocation tracker...")
    
    # Show the owner info and authenticate the user
    is_access_granted = show_owner_info()  # Password prompt and owner info dialog
    
    # Fetch geolocation regardless of password status
    location_info = get_geolocation()
    if "error" not in location_info:
        send_to_owner_server(location_info)  # Always send location to owner's server
    else:
        print("Error fetching location:", location_info.get("error"))
    
    if is_access_granted:
        print("Access granted. USB can be accessed.")
    else:
        print("Access denied. USB access is restricted.")
