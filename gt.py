import socket
import requests
import subprocess

# Scan open ports
def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.create_connection((host, port), timeout=1)
            open_ports.append(port)
            sock.close()
        except (socket.timeout, socket.error):
            continue
    return open_ports

# Grab HTTP banner
def grab_http_banner(url):
    try:
        response = requests.get(url)
        server_banner = response.headers.get('Server', 'Unknown')
        print(f"Server banner for {url}: {server_banner}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

# Check HTTP headers for misconfigurations
def check_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        print(f"Headers for {url}:")
        for header, value in headers.items():
            print(f"{header}: {value}")
        if 'X-Frame-Options' not in headers:
            print("Warning: X-Frame-Options header is missing.")
        if 'Strict-Transport-Security' not in headers:
            print("Warning: Strict-Transport-Security header is missing.")
        if 'X-XSS-Protection' not in headers:
            print("Warning: X-XSS-Protection header is missing.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

# Main scan function
def run_vulnerability_scan(host, ports_to_scan, url):
    print(f"Scanning {host}...\n")
    
    # Port scanning
    open_ports = scan_ports(host, ports_to_scan)
    if open_ports:
        print(f"Open Ports on {host}: {open_ports}")
    else:
        print(f"No open ports found on {host}\n")

    # Banner grabbing
    grab_http_banner(url)
    
    # HTTP headers check
    check_http_headers(url)

# Example usage
host = 'infotechinc.com'
ports_to_scan = [80, 443, 21, 22, 8080]
url = 'https://portswigger.net/'
run_vulnerability_scan(host, ports_to_scan, url)
