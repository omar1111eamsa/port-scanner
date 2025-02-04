import socket  # Importing the socket module for network communication
import threading  # Importing the threading module for parallel execution


def scan_port(target, port):
    """
    Function to scan a specific port on a given target IP address.
    It checks if the port is open and tries to identify the running service.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Create a socket object using IPv4 and TCP
            s.settimeout(1)  # Set a timeout of 1 second for connection attempts
            result = s.connect_ex((target, port))  # Try to connect to the specified port

            if result == 0:  # If result is 0, the port is open
                try:
                    service = socket.getservbyport(port, "tcp")  # Try to get the service name running on the port
                except OSError:
                    service = "Unknown"  # If the service name is not found, mark it as unknown
                print(f"[+] Port {port} is open ({service})")  # Print the open port and service name

    except socket.gaierror:  # Handle invalid hostname or IP address
        print("[!] Error: Invalid IP address or hostname.")
    except socket.timeout:  # Handle timeout issues
        print(f"[!] Timeout error while scanning port {port}.")
    except Exception as e:  # Catch any other unexpected errors
        print(f"[!] An unexpected error occurred: {e}")


def scan_ports_in_range(target, start_port, end_port):
    """
    Function to scan a range of ports using multiple threads.
    """
    threads = []  # List to hold threads

    # Create a thread for each port to be scanned
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


def main():
    """
    Main function to get user input and scan a range of ports on a given target.
    """

    # Prompt the user for target IP address
    target = input("Give the IP address of the target:\n")

    try:
        # Get the start and end port range from the user
        start_port = int(input("What is the Start Port: "))  
        end_port = int(input("What is the End Port: "))  # Fixed typo in the prompt

        # Validate port range
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("[!] Invalid port range. Ports must be between 0 and 65535.")
            return

        print(f"Scanning {target} from port {start_port} to {end_port}...")

        # Call the function to scan ports using multithreading
        scan_ports_in_range(target, start_port, end_port)

        print("Scan complete!")  # Print message when scanning is finished

    except ValueError:  # Handle non-numeric input for ports
        print("[!] Please enter valid numeric values for ports.")
    except Exception as e:  # Catch any unexpected errors in main function
        print(f"[!] An error occurred: {e}")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
