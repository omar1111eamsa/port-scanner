import socket  # Importing the socket module for network communication


def scan_port(target, port):
    """
    Function to scan a specific port on a given target IP address.
    It checks if the port is open and tries to identify the running service.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Create a socket object using IPv4 and TCP
        s.settimeout(1)  # Set a timeout of 1 second for connection attempts
        result = s.connect_ex((target, port))  # Try to connect to the specified port

        if result == 0:  # If result is 0, the port is open
            try:
                service = socket.getservbyport(port, "tcp")  # Try to get the service name running on the port
            except OSError:
                service = "Unknown"  # If the service name is not found, mark it as unknown
            print(f"[+] Port {port} is open ({service})")  # Print the open port and service name


def main():
    """
    Main function to get user input and scan a range of ports on a given target.
    """

    # Prompt the user for target IP address
    target = input("Give the IP address of the target:\n")

    # Get the start and end port range from the user
    start_port = int(input("What is the Start Port: "))  
    end_port = int(input("What is the End Port: "))  # Fixed typo in the prompt

    print(f"Scanning {target} from port {start_port} to {end_port}...")

    # Loop through each port in the specified range and scan it
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("Scan complete!")  # Print message when scanning is finished


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
