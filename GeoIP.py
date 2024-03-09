Import the 'requests' module for sending HTTP requests and handling responses.
import requests

def get_ip_geolocation(ip_address):
    """
    Get geolocation information for the given IP address.

    Args:
    - ip_address (str): The IP address to look up.

    Returns:
    - dict: Geolocation information.
    """
    # API endpoint for IP geolocation lookup
    api_endpoint = f"https://ipinfo.io/{ip_address}/json"

    try:
        # Make a GET request to the API
        response = requests.get(api_endpoint)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            geolocation_data = response.json()
            return geolocation_data
        else:
            print(f"Error: Unable to fetch geolocation information. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

    return None

# Usage
# Get user input for the IP address
user_input = input("Enter an IP address: ")

# Call the function to get geolocation information
geolocation_info = get_ip_geolocation(user_input)

# Display the results
if geolocation_info:
    print("\nGeolocation Information:")
    for key, value in geolocation_info.items():
        print(f"{key}: {value}")
else:
    print("Geolocation lookup failed.")
