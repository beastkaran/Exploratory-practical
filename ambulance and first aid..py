import requests

# Simulated GPS coordinates (to be replaced with actual GPS integration)
latitude = 12.3456
longitude = 78.9012

# Simulated contact number
contact_number = "+1234567890"

# To be Replaced with an actual hospital API endpoint
hospital_api_url = "https://example.com/api/send_to_hospital"

# Function to send accident data to the hospital via HTTP POST
def send_accident_data_to_hospital(latitude, longitude, contact_number):
    data = {
        "latitude": latitude,
        "longitude": longitude,
        "contact_number": contact_number
    }

    try:
        response = requests.post(hospital_api_url, json=data)
        if response.status_code == 200:
            print("Accident data sent to the hospital successfully.")
        else:
            print("Failed to send accident data to the hospital.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Simulated accident detection (to be replaced with actual detection mechanism- part of harware integration)
accident_detected = True

if accident_detected:
    print("Accident detected. Sending data to the hospital...")
    send_accident_data_to_hospital(latitude, longitude, contact_number)
    
    # Provide basic first aid guidance (replace with more detailed guidance)
    print("Please stay calm. Check for injuries and call for help.")
    print("If possible, apply pressure to stop bleeding.")
    print("Do not move the injured person if there's a chance of spinal injury.")
else:
    print("No accident detected.")

