# Importing the 're' module for regular expressions, enabling pattern matching and extraction in log parsing.
import re

def parse_log(log_file):
    # Regular expression pattern to match log entries with specific format
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+): (.*)')

    # Lists to store parsed data
    timestamps = []
    usernames = []
    messages = []

    # Read and parse each line in the log file
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                # Extracting timestamp, username, and message from the log entry
                timestamp, username, message = match.groups()
                timestamps.append(timestamp)
                usernames.append(username)
                messages.append(message)

    # Print a simple report
    print("Timestamp\t       Username\t          Message")
    print("-----------------------------------------------------------")
    for i in range(len(timestamps)):
        print(f"{timestamps[i]}\t{usernames[i]}\t\t{messages[i]}")

# Usage
log_file_path = r'D:\Python\BigLogs.log'
parse_log(log_file_path)
