import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()
        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            break
        except socket.gaierror:
            print("Invalid IP address or hostname.")
            break
        except socket.error:
            print("Couldn't connect to server.")
            break

while True:
    target = input("Enter target IP or hostname: ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

    try:
        resolved = socket.gethostbyname(target)
        scan_ports(resolved, start, end)
    except Exception as e:
        print(f"Error: {e}")
