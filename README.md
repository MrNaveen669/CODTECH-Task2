
# Project Overview: Open Port Scanner

This project demonstrates the creation of an open port scanner using Python. The scanner identifies open ports on a target host or IP address by attempting connections to specified port ranges. This tool is ideal for learning about network security, port scanning techniques, and socket programming.

# Technologies Used:
Python: For developing the script and implementing the port scanning logic.
Socket Library: For establishing TCP connections to ports on the target host.
Threading Library: For concurrent scanning to speed up the process.
# Features:
Port Scanning:Scans a specified range of ports on a target host or IP address.
Detects open ports by attempting TCP connections.

Concurrency with Threads:Utilizes Python’s threading module to scan multiple ports simultaneously for faster results.

Timeout Handling:Configurable timeout ensures quick identification of unresponsive ports.

User Input Validation:Validates user-provided inputs for target host, start port, and end port.

Customizable Scans:Users can define the port range to be scanned, enabling flexibility.

# Run the Script:
Execute the script with the following syntax:

bash
python3 port_scanner.py <target> <start_port> <end_port>

Example:
python3 port_scanner.py 192.168.1.1 1 100
# View the Output:
The script will display a list of open ports, such as:

Open Ports on 192.168.1.1:

Port 22 is open

Port 80 is open

Port 443 is open
