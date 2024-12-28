import socket
import sys
import time
import threading

usage = "python3 port_scanner.py Target Start port end port"
print("-"*70)
print("python simple port scanner")
print("-"*70)
start_time = time.time()

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try: 
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
        print("Name resolution error")
        sys.exit()

# Parse start and end ports
try:
    start_port = (sys.argv[2])
    end_port = int(sys.argv[3])
except ValueError:
    print("Error: Ports should be integers.")
    sys.exit()

# Function to scan individual ports
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)  # Set timeout to 2 seconds for the connection attempt
    
    try:
        conn = s.connect_ex((target, port))
        if conn == 0:
            print(f"Port {port} is open")
    except socket.error:
        pass  # Ignore errors related to socket connection failures
    finally:
        s.close()
 # Create a list to store references to threads
threads = []       
# Scan each port in the range using threads
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)  # Store thread reference
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print("Time elapsed: {:.2f} seconds".format(end_time - start_time))  
