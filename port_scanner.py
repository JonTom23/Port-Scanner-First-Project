import socket
from threading import Thread


target = input("Enter target IP or website: ")
target = socket.gethostbyname(target)
print(f"Scanning {target}...\n")


def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)  
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass


threads = []


for port in range(1, 1025):
    t = Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print("\nScan complete.")