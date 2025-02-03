import socket


def scan_port(target, port):
    

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"
            print(f"[+] Port {port} is open ({service})")




def main():
    target = input("Give the IP adresse of the target :\n")
    start_port = int(input("What is the Start Port : "))
    end_port = int(input("What is the End Prot :"))


    print(f"Scanning {target} from port {start_port} to {end_port}...")


    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("Scan complete!")



if __name__ == "__main__":
    main()