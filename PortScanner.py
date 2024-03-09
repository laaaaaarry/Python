# The `socket` library is used to create and manage network sockets, enabling communication with the target host over TCP for port scanning.
import socket

# Get user input for the target host and port range
target_host = input("Enter target host: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

# Display a message indicating the start of the port scanning process
print(f"Scanning ports on {target_host}...\n")

# Iterate through the specified port range
for port in range(start_port, end_port + 1):
    # Create a socket object for TCP connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout for the connection attempt (1 second)
    sock.settimeout(1)

    # Attempt to connect to the target host and port
    result = sock.connect_ex((target_host, port))

    # Check the result of the connection attempt
    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed")

    # Close the socket connection
    sock.close()

