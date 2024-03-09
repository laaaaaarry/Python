# Import the 'requests' module for sending HTTP requests and working with responses
import requests

def check_http_status(urls):
    """
    Send HTTP requests to a list of URLs and print the status codes.

    Args:
    - urls (list): A list of URLs to check.

    Returns:
    - dict: A dictionary mapping each URL to its corresponding HTTP status code.
    """
    # Dictionary to store URL-status code pairs
    status_codes = {}

    try:
        # Iterate through the list of URLs
        for url in urls:
            # Send an HTTP GET request to the URL
            response = requests.get(url)

            # Get the status code from the response
            status_code = response.status_code

            # Print the URL and its status code
            print(f"{url} - Status Code: {status_code}")

            # Store the URL and status code in the dictionary
            status_codes[url] = status_code

    except Exception as e:
        print(f"Error: {e}")

    return status_codes

# Usage
# Provide a list of URLs to check
url_list = ["https://www.microsoft.com", "https://www.google.com", "https://www.eccouncil.com"]

# Call the function to check HTTP status codes
result_status_codes = check_http_status(url_list)

# Display the result
print("\nResult Status Codes:")
print(result_status_codes)
