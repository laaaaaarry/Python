# Import the 'platform' module to retrieve information about the operating system
import platform
# Import the 'os' module for various operating system-related functionalities
import os
# Import the 'psutil' module to access system details, such as memory information
import psutil

def get_system_information():
    """
    Retrieve and print basic system information.

    Returns:
    - dict: Basic system information.
    """
    # Get the system platform (e.g., 'Windows', 'Linux')
    os_name = platform.system()

    # Get the system version (e.g., '10.0.19041' for Windows)
    os_version = platform.version()

    # Get the machine's network name (hostname)
    hostname = platform.node()

    # Get the machine's processor information
    processor = platform.processor()

    # Get the total physical memory (RAM) in bytes
    total_memory = psutil.virtual_memory().total

    # Convert bytes to gigabytes for easier readability
    total_memory_gb = round(total_memory / (1024 ** 3), 2)

    # Create a dictionary with the gathered information
    system_info = {
        'OS': f'{os_name} {os_version}',
        'Hostname': hostname,
        'Processor': processor,
        'Total Memory': f'{total_memory_gb} GB'
    }

    return system_info

# Usage
# Call the function to get system information
system_information = get_system_information()

# Display the results
print("\nBasic System Information:")
for key, value in system_information.items():
    print(f"{key}: {value}")
