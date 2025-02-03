Port Scanner

Description

This project is a simple Python Port Scanner that scans a given IP address for open ports within a specified range. It uses the socket library to attempt connections and identifies common services running on open ports.

Features

Scans a target IP for open ports.

Identifies the service running on open ports (if known).

Uses a timeout to avoid long waits.

Simple and lightweight.

How to Use

Run the script

python port_scanner.py

Provide user inputs:

Enter the target IP address.

Enter the start port.

Enter the end port.

The script will scan the ports and display the open ports along with their corresponding services.

Example Output

Give the IP address of the target:
127.0.0.1
What is the Start Port:
50
What is the End Port:
10000
Scanning 127.0.0.1 from port 50 to 10000...
[+] Port 80 is open (http)
Scan complete!

Future Improvements

Add multi-threading for faster scanning.

Save scan results to a file.

Enhance error handling.

ons

Feel free to fork, submit pull requests, or suggest improvements to make this tool even better!

